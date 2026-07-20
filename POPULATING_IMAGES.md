# Populating figures

Chapters are produced in two passes:

1. **Text + captions** — the pages carry `<<FIGURE: ... >>` placeholders that
   describe the figure that belongs there.
2. **Images** (this step) — an editor fills each placeholder with a real image.

Run the bundled tool from this folder (Python 3.9+, no installation needed):

```bash
python image_populator.py --dir docs
```

It opens a small app in your browser. For each figure you can **paste from the
clipboard** (e.g. a region snipped from PACS), **choose a file**, **drag-and-drop**,
or **search open-licence sources** (Wikimedia Commons, Openverse). Add a caption
and attribution, then save — the image is written into `docs/img/` and the
placeholder is replaced with a proper figure.

> **⚠️ Patient data.** An image snipped from PACS can contain patient-identifiable
> information. Confirm every locally-supplied image is anonymised and appropriately
> consented before saving — the tool asks you to tick a box to that effect.

> **Note.** Re-running the publish step overwrites a chapter's page from source, so
> populate images **after** the final publish of that chapter and do not re-publish
> it afterwards.
