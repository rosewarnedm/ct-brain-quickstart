#!/usr/bin/env python3
"""image_populator.py — editor tool to fill ``<<FIGURE>>`` placeholders with images.

This is the **image-harvesting pass**: run it near the end of production, after the
chapters and their figure captions have been generated. It is deliberately
**standalone** — Python 3.9+ standard library only, no ``pip install`` — so an
editor can download this single file from the published site repository and run it
without the rest of the generator toolchain.

It launches a small local web app in your browser. For each ``<<FIGURE: …>>``
placeholder found in the Markdown, you supply an image by:

  • pasting from the clipboard (e.g. a region snipped from PACS) — Ctrl/Cmd-V
  • choosing a file — opens your operating system's file browser — or drag-and-drop
  • searching open-licence sources (Wikimedia Commons, Openverse)

…then add a caption and attribution and save. The image is written into an
``img/`` folder beside the page and the placeholder is replaced with a proper
Markdown figure. Progress is written to disk after every figure, so you can stop
and resume at any time.

⚠️  PATIENT DATA. An image snipped from PACS can contain patient-identifiable
information (names, dates, MRNs burnt into the pixels, or in overlays). You are
asked to confirm, for every locally-supplied image, that it is anonymised and
that appropriate consent / information-governance is in place before it is saved.

Run:
  python image_populator.py                 # scan the current folder (and ./docs)
  python image_populator.py --dir docs      # scan a specific folder
  python image_populator.py --port 8765     # choose the local port
  python image_populator.py --no-web        # disable the web-search source
"""

import argparse
import base64
import json
import re
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# ---------------------------------------------------------------------------
# Shared constants and small helpers
# ---------------------------------------------------------------------------

USER_AGENT = (
    "generate-atlases-image-populator/1.0 (educational teaching-atlas figure curation)"
)
TIMEOUT = 30

FIGURE_RE = re.compile(r"<<FIGURE:(.*?)>>", re.DOTALL)
FREE_LICENCE_RE = re.compile(r"\b(cc0|public domain|cc[\s-]?by(?:[\s-]?sa)?)\b", re.I)
NC_RE = re.compile(r"\bnc\b|non[\s-]?commercial", re.I)
ND_RE = re.compile(r"\bnd\b|no[\s-]?deriv", re.I)

MIME_EXT = {
    "image/jpeg": ".jpg", "image/jpg": ".jpg", "image/png": ".png",
    "image/gif": ".gif", "image/svg+xml": ".svg", "image/webp": ".webp",
}

# Resolved at startup in main().
BASE_DIR: Path = Path(".")
WEB_ENABLED = True


def classify_licence(licence: str, allow_nc: bool = False) -> "bool | None":
    if not licence:
        return None
    if not FREE_LICENCE_RE.search(licence):
        return None
    if not allow_nc and NC_RE.search(licence):
        return False
    if ND_RE.search(licence):
        return False
    return True


def _strip_html(s: str) -> str:
    import html
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def _http_get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


# ---------------------------------------------------------------------------
# Placeholder scanning
# ---------------------------------------------------------------------------

def parse_placeholder(body: str) -> dict:
    parts = [p.strip() for p in body.split("::")]
    description = parts[0] if parts else ""
    caption = parts[1] if len(parts) > 1 and parts[1] else description
    terms = parts[2] if len(parts) > 2 and parts[2] else description
    return {"raw": f"<<FIGURE:{body}>>", "description": description,
            "caption": caption, "terms": terms}


def markdown_files(base: Path) -> "list[Path]":
    return sorted(p for p in base.rglob("*.md") if p.is_file())


def scan_figures(base: Path) -> "list[dict]":
    """Every unresolved placeholder across the tree, tagged with its file."""
    out: list[dict] = []
    for path in markdown_files(base):
        text = path.read_text(encoding="utf-8")
        for m in FIGURE_RE.finditer(text):
            ph = parse_placeholder(m.group(1))
            ph["file"] = str(path.relative_to(base))
            out.append(ph)
    return out


# ---------------------------------------------------------------------------
# Web search providers (standalone copies; no dependency on figure_helper.py)
# ---------------------------------------------------------------------------

def search_wikimedia(terms: str, limit: int) -> "list[dict]":
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": terms, "gsrnamespace": "6", "gsrlimit": str(limit),
        "prop": "imageinfo", "iiprop": "url|extmetadata|mime|size", "iiurlwidth": "1024",
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    try:
        data = json.loads(_http_get(url).decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [{"error": f"Wikimedia search failed: {exc}"}]
    out = []
    for page in ((data.get("query") or {}).get("pages") or {}).values():
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata") or {}
        licence = _strip_html((meta.get("LicenseShortName") or {}).get("value", ""))
        artist = _strip_html((meta.get("Artist") or {}).get("value", ""))
        credit = _strip_html((meta.get("Credit") or {}).get("value", ""))
        ok = classify_licence(licence)
        if ok is False:
            continue
        attribution = ", ".join(p for p in (artist or credit, "via Wikimedia Commons") if p)
        out.append({
            "source": "Wikimedia Commons", "title": page.get("title", ""),
            "view_url": info.get("thumburl") or info.get("url", ""),
            "download_url": info.get("url", ""),
            "page_url": info.get("descriptionurl") or info.get("url", ""),
            "licence": licence or "unstated", "attribution": attribution,
            "licence_ok": ok,
        })
    return out


_OV_NAMES = {"cc0": "CC0", "pdm": "Public domain", "by": "CC BY", "by-sa": "CC BY-SA",
             "by-nd": "CC BY-ND", "by-nc": "CC BY-NC", "by-nc-sa": "CC BY-NC-SA",
             "by-nc-nd": "CC BY-NC-ND"}


def search_openverse(terms: str, limit: int) -> "list[dict]":
    params = {"q": terms, "page_size": str(limit), "license_type": "commercial,modification"}
    url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(params)
    try:
        data = json.loads(_http_get(url).decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [{"error": f"Openverse search failed: {exc}"}]
    out = []
    for item in (data.get("results") or []):
        code = (item.get("license") or "").lower()
        ver = item.get("license_version") or ""
        licence = _OV_NAMES.get(code, code.upper())
        if ver and code not in ("cc0", "pdm"):
            licence = f"{licence} {ver}".strip()
        ok = classify_licence(licence)
        if ok is False:
            continue
        attribution = (item.get("attribution") or "").split(" is licensed under")[0].strip()
        out.append({
            "source": "Openverse", "title": item.get("title") or "",
            "view_url": item.get("thumbnail") or item.get("url", ""),
            "download_url": item.get("url", ""),
            "page_url": item.get("foreign_landing_url", ""),
            "licence": licence or "unstated",
            "attribution": attribution or (item.get("creator") or ""),
            "licence_ok": ok,
        })
    return out


def do_search(query: str) -> "list[dict]":
    results, errors = [], []
    for fn in (search_wikimedia, search_openverse):
        for r in fn(query, 6):
            (errors if "error" in r else results).append(r)
    if errors and not results:
        return [{"error": "; ".join(e["error"] for e in errors)}]
    return results


# ---------------------------------------------------------------------------
# Saving: write image, rewrite placeholder
# ---------------------------------------------------------------------------

def _chapter_prefix(name: str) -> str:
    m = re.search(r"[Cc]hapter[_ ]?(\d+)", name)
    return f"ch{int(m.group(1)):02d}" if m else "fig"


def _slug(text: str, limit: int = 40) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", (text or "").lower()).strip("_")
    return s[:limit].strip("_") or "figure"


def img_target(md_path: Path):
    """Where images go and how they are referenced, depending on the site layout.

    Under a Jekyll ``docs/`` directory (the published Just-the-Docs site) images
    are written to ``docs/img/`` and referenced with a baseurl-safe Liquid tag,
    matching publish_to_quickstart.py. Otherwise a plain relative ``img/`` link is
    used (the pre-publish atlas convention).
    """
    for parent in md_path.parents:
        if parent.name == "docs":
            return parent / "img", "jekyll"
    return md_path.parent / "img", "plain"


def make_ref(mode: str, name: str) -> str:
    if mode == "jekyll":
        return f"{{{{ '/docs/img/{name}' | relative_url }}}}"
    return f"img/{name}"


def unique_path(img_dir: Path, stem: str, ext: str) -> Path:
    p = img_dir / f"{stem}{ext}"
    n = 2
    while p.exists():
        p = img_dir / f"{stem}_{n}{ext}"
        n += 1
    return p


def figure_markdown(caption: str, ref: str, attribution: str, licence: str, url: str) -> str:
    bits = [b for b in (attribution.strip(), licence.strip()) if b]
    credit = " — ".join(bits) if bits else "source not specified"
    src = f" {url.strip()}" if url.strip() else ""
    return f"![{caption}]({ref})\n\n*Figure: {caption}. Source: {credit}.{src}*"


def _decode_data_url(data_url: str):
    """Return (bytes, ext) for a data: URL or bare base64 string."""
    mime = ""
    b64 = data_url
    if data_url.startswith("data:"):
        header, _, b64 = data_url.partition(",")
        mime = header[5:].split(";")[0]
    return base64.b64decode(b64), MIME_EXT.get(mime, "")


def do_save(payload: dict) -> dict:
    rel_file = payload["file"]
    md_path = (BASE_DIR / rel_file).resolve()
    if BASE_DIR.resolve() not in md_path.parents and md_path != BASE_DIR.resolve():
        return {"ok": False, "error": "refusing to write outside the scanned folder"}
    if not md_path.is_file():
        return {"ok": False, "error": f"file not found: {rel_file}"}

    raw = payload["raw"]
    text = md_path.read_text(encoding="utf-8")
    if raw not in text:
        return {"ok": False, "error": "placeholder already resolved or not found"}

    data, ext_from_mime = _decode_data_url(payload["image"])
    ext = ext_from_mime or (Path(payload.get("filename", "")).suffix.lower() or ".png")
    if ext not in MIME_EXT.values():
        ext = ".png"

    img_dir, mode = img_target(md_path)
    img_dir.mkdir(parents=True, exist_ok=True)
    dest = unique_path(img_dir, f"{_chapter_prefix(md_path.name)}_{_slug(payload.get('caption'))}", ext)
    dest.write_bytes(data)

    caption = payload.get("caption") or "figure"
    md = figure_markdown(caption, make_ref(mode, dest.name),
                         payload.get("attribution", ""), payload.get("licence", ""),
                         payload.get("source_url", ""))
    md_path.write_text(text.replace(raw, md, 1), encoding="utf-8")

    remaining = len(scan_figures(BASE_DIR))
    return {"ok": True, "image": str(dest.relative_to(BASE_DIR)), "remaining": remaining}


# ---------------------------------------------------------------------------
# HTTP server
# ---------------------------------------------------------------------------

INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Image Populator</title>
<style>
  :root { --b:#2563eb; --g:#16a34a; --r:#dc2626; --line:#e5e7eb; }
  * { box-sizing: border-box; }
  body { font-family: system-ui, sans-serif; margin: 0; color:#111; background:#f8fafc; }
  header { background:#0f172a; color:#fff; padding:10px 16px; display:flex; justify-content:space-between; align-items:center; }
  header .warn { color:#fca5a5; font-size:13px; }
  main { display:flex; gap:16px; padding:16px; align-items:flex-start; }
  #queue { width:300px; flex:none; background:#fff; border:1px solid var(--line); border-radius:8px; max-height:80vh; overflow:auto; }
  #queue h3 { margin:0; padding:10px; border-bottom:1px solid var(--line); font-size:14px; }
  .qitem { padding:8px 10px; border-bottom:1px solid var(--line); cursor:pointer; font-size:13px; }
  .qitem:hover { background:#f1f5f9; }
  .qitem.active { background:#dbeafe; }
  .qitem .file { color:#64748b; font-size:11px; }
  #panel { flex:1; background:#fff; border:1px solid var(--line); border-radius:8px; padding:16px; }
  label { display:block; font-size:12px; font-weight:600; margin:12px 0 4px; color:#334155; }
  input[type=text], textarea { width:100%; padding:8px; border:1px solid var(--line); border-radius:6px; font-size:14px; font-family:inherit; }
  .row { display:flex; gap:16px; }
  .row > div { flex:1; }
  #drop { border:2px dashed #94a3b8; border-radius:8px; padding:18px; text-align:center; color:#64748b; background:#f8fafc; margin-top:6px; }
  #drop.hot { border-color:var(--b); background:#eff6ff; }
  #preview { max-width:100%; max-height:320px; margin-top:10px; display:none; border:1px solid var(--line); border-radius:6px; }
  button { font:inherit; padding:8px 14px; border:0; border-radius:6px; cursor:pointer; }
  .primary { background:var(--b); color:#fff; } .primary:disabled { background:#93c5fd; cursor:not-allowed; }
  .ghost { background:#e2e8f0; }
  .bar { margin-top:16px; display:flex; gap:8px; }
  #results { display:flex; flex-wrap:wrap; gap:8px; margin-top:8px; }
  .cand { width:150px; border:1px solid var(--line); border-radius:6px; padding:6px; cursor:pointer; font-size:11px; }
  .cand:hover { border-color:var(--b); }
  .cand img { width:100%; height:90px; object-fit:cover; border-radius:4px; }
  .lic { font-weight:600; } .ok { color:var(--g); } .warnlic { color:#b45309; }
  .gov { background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:10px; margin-top:12px; font-size:13px; }
  #msg { margin-left:auto; font-size:13px; align-self:center; }
  small.hint { color:#64748b; font-weight:400; }
</style></head>
<body>
<header>
  <strong>🖼️ Image Populator</strong>
  <span class="warn">Confirm every PACS/local image is anonymised &amp; consented before saving.</span>
</header>
<main>
  <div id="queue"><h3>Figures</h3><div id="qlist"></div></div>
  <div id="panel">
    <div id="empty" style="display:none; color:#16a34a; font-weight:600;">🎉 No unresolved figures. You're done.</div>
    <div id="editor">
      <div><strong id="desc"></strong></div>
      <div class="file" style="color:#64748b; font-size:12px;" id="curfile"></div>

      <div class="row">
        <div><label>Caption</label><input type="text" id="caption"></div>
      </div>
      <div class="row">
        <div><label>Attribution / source <small class="hint">(author, or "local teaching case")</small></label><input type="text" id="attribution"></div>
        <div><label>Licence <small class="hint">(if applicable)</small></label><input type="text" id="licence"></div>
      </div>
      <label>Source URL <small class="hint">(optional)</small></label><input type="text" id="source_url">

      <label>Image <small class="hint">— paste (Ctrl/Cmd-V), drop, or choose a file</small></label>
      <div id="drop">
        Paste from clipboard, drag an image here, or
        <input type="file" id="file" accept="image/*">
      </div>
      <img id="preview">

      <div class="gov" id="govbox" style="display:none;">
        <label style="display:flex; gap:8px; align-items:flex-start; margin:0; font-weight:400;">
          <input type="checkbox" id="gov" style="margin-top:2px;">
          I confirm this image contains no patient-identifiable information and that
          appropriate consent / information-governance is in place.
        </label>
      </div>

      <label>Search open-licence sources <small class="hint">(Wikimedia Commons, Openverse)</small></label>
      <div class="row">
        <div style="flex:3;"><input type="text" id="query" placeholder="e.g. usual interstitial pneumonia HRCT honeycombing"></div>
        <div style="flex:1;"><button class="ghost" id="searchbtn" style="width:100%;">Search</button></div>
      </div>
      <div id="results"></div>

      <div class="bar">
        <button class="primary" id="save" disabled>Save figure</button>
        <button class="ghost" id="skip">Skip</button>
        <span id="msg"></span>
      </div>
    </div>
  </div>
</main>
<script>
let figures = [], idx = 0, image = null, source = null, webEnabled = true;

async function api(path, body) {
  const r = await fetch(path, {method: body ? 'POST' : 'GET',
    headers: {'Content-Type':'application/json'}, body: body ? JSON.stringify(body) : undefined});
  return r.json();
}
function $(id){ return document.getElementById(id); }

async function load() {
  const data = await api('/api/figures');
  figures = data.figures; webEnabled = data.web;
  if (!webEnabled) { $('query').disabled = true; $('searchbtn').disabled = true; }
  render();
}
function render() {
  const list = $('qlist'); list.innerHTML = '';
  figures.forEach((f, i) => {
    const d = document.createElement('div');
    d.className = 'qitem' + (i===idx ? ' active' : '');
    d.innerHTML = '<div>'+f.description+'</div><div class="file">'+f.file+'</div>';
    d.onclick = () => { idx = i; show(); };
    list.appendChild(d);
  });
  if (figures.length === 0) { $('editor').style.display='none'; $('empty').style.display='block'; return; }
  if (idx >= figures.length) idx = 0;
  show();
}
function show() {
  const f = figures[idx];
  $('desc').textContent = f.description;
  $('curfile').textContent = f.file;
  $('caption').value = f.caption || '';
  $('attribution').value = ''; $('licence').value = ''; $('source_url').value = '';
  $('query').value = f.terms || '';
  $('results').innerHTML = ''; $('msg').textContent = '';
  setImage(null, null);
  render_active();
}
function render_active() {
  document.querySelectorAll('.qitem').forEach((el,i)=>el.classList.toggle('active', i===idx));
}
function setImage(dataUrl, src) {
  image = dataUrl; source = src;
  const p = $('preview');
  if (dataUrl) { p.src = dataUrl; p.style.display='block'; } else { p.style.display='none'; }
  $('govbox').style.display = (src === 'local') ? 'block' : 'none';
  if (src !== 'local') $('gov').checked = false;
  refreshSave();
}
function refreshSave() {
  const needGov = (source === 'local');
  $('save').disabled = !(image && (!needGov || $('gov').checked));
}

// clipboard paste
window.addEventListener('paste', e => {
  for (const item of e.clipboardData.items) {
    if (item.type.startsWith('image/')) {
      const r = new FileReader();
      r.onload = () => setImage(r.result, 'local');
      r.readAsDataURL(item.getAsFile());
      $('msg').textContent = 'Pasted from clipboard.';
    }
  }
});
// file chooser
$('file').addEventListener('change', e => {
  const file = e.target.files[0]; if (!file) return;
  const r = new FileReader(); r.onload = () => setImage(r.result, 'local'); r.readAsDataURL(file);
});
// drag & drop
const drop = $('drop');
['dragover','dragenter'].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.add('hot'); }));
['dragleave','drop'].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.remove('hot'); }));
drop.addEventListener('drop', e => {
  const file = e.dataTransfer.files[0]; if (!file || !file.type.startsWith('image/')) return;
  const r = new FileReader(); r.onload = () => setImage(r.result, 'local'); r.readAsDataURL(file);
});
$('gov').addEventListener('change', refreshSave);

// web search
$('searchbtn').addEventListener('click', async () => {
  $('results').innerHTML = 'Searching…';
  const data = await api('/api/search', {query: $('query').value});
  const box = $('results'); box.innerHTML = '';
  if (data.error) { box.textContent = data.error; return; }
  if (!data.results.length) { box.textContent = 'No candidates found.'; return; }
  data.results.forEach(c => {
    const el = document.createElement('div'); el.className = 'cand';
    const licClass = c.licence_ok === true ? 'ok' : 'warnlic';
    el.innerHTML = '<img src="'+c.view_url+'" loading="lazy">'
      + '<div class="lic '+licClass+'">'+c.licence+'</div>'
      + '<div>'+(c.title||'').slice(0,60)+'</div>'
      + '<div style="color:#64748b;">'+c.source+'</div>';
    el.onclick = async () => {
      $('msg').textContent = 'Fetching image…';
      const f = await api('/api/fetch', {url: c.download_url});
      if (f.error) { $('msg').textContent = f.error; return; }
      setImage(f.image, 'web');
      $('attribution').value = c.attribution || '';
      $('licence').value = c.licence || '';
      $('source_url').value = c.page_url || '';
      $('msg').textContent = 'Loaded — verify it shows the finding, then Save.';
    };
    box.appendChild(el);
  });
});

// save / skip
$('save').addEventListener('click', async () => {
  const f = figures[idx];
  $('save').disabled = true; $('msg').textContent = 'Saving…';
  const res = await api('/api/save', {
    file: f.file, raw: f.raw, image,
    caption: $('caption').value, attribution: $('attribution').value,
    licence: $('licence').value, source_url: $('source_url').value,
  });
  if (!res.ok) { $('msg').textContent = 'Error: ' + res.error; refreshSave(); return; }
  figures.splice(idx, 1);
  $('msg').textContent = 'Saved → ' + res.image + '  (' + res.remaining + ' left)';
  render();
});
$('skip').addEventListener('click', () => { idx = (idx + 1) % Math.max(figures.length,1); render(); });

load();
</script>
</body></html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # keep the console quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj).encode("utf-8"), "application/json")

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length).decode("utf-8")) if length else {}

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/index"):
            self._send(200, INDEX_HTML.encode("utf-8"), "text/html; charset=utf-8")
        elif self.path == "/api/figures":
            self._json({"figures": scan_figures(BASE_DIR), "web": WEB_ENABLED})
        else:
            self._send(404, b"not found", "text/plain")

    def do_POST(self):
        try:
            payload = self._read_json()
            if self.path == "/api/search":
                self._json(_search_response(payload.get("query", "")))
            elif self.path == "/api/fetch":
                self._json(_fetch_response(payload.get("url", "")))
            elif self.path == "/api/save":
                self._json(do_save(payload))
            else:
                self._json({"error": "unknown endpoint"}, 404)
        except Exception as exc:  # noqa: BLE001
            self._json({"error": str(exc)}, 500)


def _search_response(query: str) -> dict:
    if not WEB_ENABLED:
        return {"error": "web search disabled"}
    results = do_search(query)
    errs = [r["error"] for r in results if "error" in r]
    ok = [r for r in results if "error" not in r]
    return {"results": ok, "error": "; ".join(errs)} if errs and not ok else {"results": ok}


def _fetch_response(url: str) -> dict:
    if not url:
        return {"error": "no url"}
    try:
        data = _http_get(url)
    except Exception as exc:  # noqa: BLE001
        return {"error": f"fetch failed: {exc}"}
    ext = Path(urllib.parse.urlparse(url).path).suffix.lower()
    mime = next((m for m, e in MIME_EXT.items() if e == ext), "image/jpeg")
    return {"image": f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    global BASE_DIR, WEB_ENABLED
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dir", default=".", help="folder to scan for Markdown (default: current)")
    parser.add_argument("--port", type=int, default=8765, help="local port (default: 8765)")
    parser.add_argument("--no-web", action="store_true", help="disable the web-search source")
    parser.add_argument("--no-browser", action="store_true", help="do not auto-open the browser")
    args = parser.parse_args()

    BASE_DIR = Path(args.dir).resolve()
    WEB_ENABLED = not args.no_web
    if not BASE_DIR.is_dir():
        raise SystemExit(f"{BASE_DIR} is not a folder")

    n = len(scan_figures(BASE_DIR))
    url = f"http://127.0.0.1:{args.port}/"
    print(f"Image Populator — scanning {BASE_DIR}")
    print(f"  {n} unresolved <<FIGURE>> placeholder(s) found.")
    print(f"  Open {url} in your browser." + ("" if args.no_browser else " (opening…)"))
    print("  Press Ctrl-C to stop.")
    if not args.no_browser:
        try:
            webbrowser.open(url)
        except Exception:  # noqa: BLE001
            pass
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
