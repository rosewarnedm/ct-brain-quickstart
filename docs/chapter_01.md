---
layout: default
title: "Chapter 01: CT Physics and Technique"
nav_order: 1
---

# Chapter 1: CT Physics and Technique — Practical Summary for Acute Brain CT

## 1. CT Physics: What Actually Matters at the Workstation

**Hounsfield Units (HU) are the language of CT.** Every voxel is expressed relative to water:
- <⚠️ [#1 REVIEW: ]<Air = −1000 HU; water = 0 HU; CSF = 0–15 HU; white matter ~20–30 HU; grey matter ~30–45 HU; acute clotted blood ~60–80 HU; iodinated contrast ~150–300 HU; calcification often 150–400 HU; cortical bone 1000–3000 HU.>>
- **Measure HU with an ROI** when in doubt — don't guess. This is the single most useful habit when distinguishing haemorrhage, calcification, contrast staining and pseudo-SAH.

**kVp and mAs:**
- <⚠️ [#2 REVIEW: ]<Standard non-contrast head CT is acquired at 120 kVp.>> Higher kVp (140) reduces posterior fossa beam hardening in large patients.
- Lower kVp (100–110) boosts iodine conspicuity for CTA but increases noise. Apparent HU of blood and iodine rises at lower kVp — keep this in mind when comparing scans.

**Reconstruction kernels:**
- Soft/standard kernel for parenchyma; sharp/bone kernel for fractures and skull base. Always review both.
- Iterative reconstruction reduces noise and improves detection of subtle early ischaemic change, particularly in the posterior fossa.

**Spatial vs low-contrast resolution:**
- Detecting subtle hypoattenuation (loss of insular ribbon, early infarct) needs **low-contrast resolution** — favour soft kernels, adequate mAs, IR.
- Detecting small haemorrhages, fractures, hyperdense vessels needs **spatial resolution** — thin slices, sharper kernels.

## 2. Artefacts You Must Recognise

- **Beam hardening (skull base/posterior fossa):** dark streaks mimicking or masking infarct/haemorrhage. Mitigate with thin slices, IR, dedicated posterior fossa windows. Have a low threshold for MRI if clinical suspicion persists.
- **Metal streak (clips, coils, dental):** use MAR algorithms or dual-energy high-keV monoenergetic reconstructions.
- **Partial volume averaging:** classic cause of missed vertex SDH and small sulcal SAH — use thin slices and coronal/sagittal MPRs.
- **Motion:** repeat affected slabs only, not the whole study.
- **Pseudo-SAH:** diffuse cerebral oedema makes cisterns *look* hyperdense relative to dark parenchyma. <⚠️ [#3 REVIEW: ]<Pseudo-SAH measures ~30–40 HU in basal cisterns; true acute SAH is typically >50 HU.>>

## 3. Tissue Attenuation: Pattern Recognition

### Ischaemia (time course on NCCT)
- <⚠️ [#4 REVIEW: ]<0–6 h: subtle hypoattenuation (only 2–5 HU drop), loss of insular ribbon, obscuration of lentiform nucleus, sulcal effacement; hyperdense artery sign 45–75 HU if thrombus present.>>
- 6–24 h: well-demarcated low attenuation, increasing mass effect.
- 3–5 days: peak mass effect.
- Weeks: encephalomalacia, CSF-density.

**Cytotoxic oedema** (acute infarct): grey + white matter, follows vascular territory, loss of grey–white differentiation.
**Vasogenic oedema** (tumour, abscess): white matter, finger-like, spares cortex early.

### Haemorrhage by age
- **IPH:** <⚠️ [#5 REVIEW: ]<Hyperacute (<6 h) uncoagulated blood may be only 30–50 HU and less conspicuous; acute (6 h–3 d) ~60–80 HU; subacute (3 d–2 w) drops to 30–60 HU; chronic (>2–3 w) approaches CSF density (0–20 HU).>>
- **SAH:** <⚠️ [#6 REVIEW: ]<Fresh SAH is 50–70 HU; sensitivity of NCCT is highest within 6 hours of ictus and declines thereafter, becoming isodense by 1–2 weeks.>>
- **SDH:** <⚠️ [#7 REVIEW: ]<Acute crescentic SDH 50–80 HU; early subacute (1–3 weeks) is often isodense to cortex and easily missed; chronic (>3 weeks) is 0–20 HU.>> Use coronal MPRs and subdural windows for the vertex.
- **EDH:** biconvex, sharply limited by sutures, acute 50–80 HU.

### Calcification, fat, air, protein
- Calcification: very high HU, unchanged with contrast.
- Fat: negative HU → think dermoid, lipoma, surgical packing.
- Air: −1000 HU → trauma, surgery, infection.
- Proteinaceous fluid (e.g. colloid cyst): 20–60 HU, can mimic blood — judge by location and morphology.

## 4. Standard Non-contrast Head CT Technique

**Positioning:** supine, head immobilised, gantry tilted parallel to the supraorbital–meatal line to spare the lenses and reduce dental artefact.

**Typical adult parameters:**
- <⚠️ [#8 REVIEW: ]<120 kVp; 250–400 mAs (or modulated); CTDIvol ~40–60 mGy.>>
- Collimation 0.5–1.25 mm; pitch 0.5–1.0.

**Reconstructions to review on every study:**
- Axial brain (soft kernel) 4–5 mm.
- Thin (0.5–1 mm) bone kernel for fractures.
- Coronal and sagittal MPRs (essential for vertex SDH, skull base fractures).
- Thin posterior fossa slab (2–3 mm).

**Window/level presets:**
- <⚠️ [#9 REVIEW: ]<Brain: WW 80, WL 40.>>
- <⚠️ [#10 REVIEW: ]<Subdural/blood: WW 200–300, WL 50–80.>>
- <⚠️ [#11 REVIEW: ]<Bone: WW 2500–4000, WL 500–700.>>

Always do at least two passes (parenchyma + bone) and adjust windows for SAH, vertex SDH and posterior fossa.

## 5. Contrast-enhanced Techniques

### CECT
- 60–100 mL iodinated contrast, scan at 60–90 s.
- **Pitfall:** post-thrombectomy contrast staining mimics haemorrhage. Resolve with dual-energy (iodine map / virtual non-contrast) or short-interval follow-up — <⚠️ [#12 REVIEW: ]<iodine washes out within 24 hours, blood does not.>>

### CTA head and neck
- Coverage **aortic arch to vertex**; 60–80 mL at 4–6 mL/s, saline chaser.
- <⚠️ [#13 REVIEW: ]<Bolus tracking ROI in aorta/carotid, trigger at 100–150 HU; acquire caudo-cranially to limit venous contamination.>>
- Indicated in suspected LVO, aneurysm, dissection, vasospasm, traumatic vascular injury.
- Watch for carotid pseudo-occlusion in proximal high-grade stenosis — correlate with delayed phases.

### CTV
- Venous phase (45–60 s) imaging for suspected CVST.
- <⚠️ [#14 REVIEW: ]<Hyperdense sinus on NCCT >70–80 HU is suggestive of acute thrombus, but high haematocrit/dehydration can mimic.>>

### CTP
- Used for extended-window or wake-up stroke selection for thrombectomy.
- <⚠️ [#15 REVIEW: ]<Standard automated thresholds: ischaemic core = relative CBF <30%; penumbra = Tmax >6 s with preserved CBV.>>
- Always cross-check against NCCT and CTA. Leukoaraiosis, motion, and proximal stenosis distort maps.

### Dual-energy CT
- Best tool for **iodine vs haemorrhage** post-intervention.
- Monoenergetic high-keV reduces calcium/metal blooming.

## 6. Critical Pitfalls — Don't Miss These

- **Subtle SAH:** thin slices and meticulous review of basal cisterns. Compare cistern HU to true SAH thresholds (see above).
- **Hyperdense artery sign vs mimics:** <⚠️ [#16 REVIEW: ]<true thrombus is 45–75 HU and >1.2–1.5× the contralateral lumen density>>; calcification is much denser (>100–150 HU) and blooms on bone kernel.
- **Posterior fossa:** beam hardening hides brainstem/cerebellar pathology — low threshold for MRI.
- **Vertex SDH:** use coronal MPRs and subdural windows.
- **Isodense subacute SDH (1–3 weeks):** look for sulcal effacement, mass effect, grey–white interface displacement.
- **Contrast staining post-thrombectomy:** confirm with dual-energy or 24-hour follow-up before calling haemorrhage.
- **Basal ganglia calcification vs haemorrhage:** symmetric, very high HU, no oedema = calcification.

## 7. Differential by Attenuation

**Hyperdense:** blood (50–80 HU), calcification (>100–150 HU), iodine (150–300 HU), proteinaceous cyst (30–90 HU), thrombus (45–75 HU).

**Hypodense:** acute infarct (subtle 2–5 HU drop early, ~10–15 HU later), vasogenic oedema (white matter, finger-like), encephalomalacia (CSF-density), hygroma.

**Mixed:** subacute SDH with haematocrit levels; haemorrhagic transformation of infarct.

## 8. Reporting Checklist for Acute NCCT

1. Technical adequacy (motion, coverage, windowing).
2. Scalp, fractures (bone windows), sinuses, orbits.
3. Extra-axial spaces — SDH/EDH; cisterns/sulci for SAH.
4. Ventricles — size, blood, levels.
5. Parenchyma — <⚠️ [#17 REVIEW: ]<grey–white differentiation; calculate ASPECTS in anterior circulation stroke>>.
6. Haemorrhage — location, volume, IVH, mass effect, herniation.
7. Vessels — hyperdense artery/sinus signs.
8. Mass effect — midline shift, basal cistern patency, herniation.
9. **Action items:** thrombolysis/thrombectomy eligibility, neurosurgical alert (EDH, large SDH, posterior fossa haemorrhage).

## 9. Clinical Pathway Integration

- **Hyperacute stroke:** NCCT to exclude haemorrhage → ASPECTS → CTA for LVO → CTP if extended window. <⚠️ [#18 REVIEW: ]<ASPECTS ≤5–6 generally indicates a large established infarct that may exclude the patient from reperfusion therapy, depending on local protocol.>>
- **Head injury:** NCCT with bone reformats; CTA if vascular injury suspected.
- **Suspected SAH:** <⚠️ [#19 REVIEW: ]<NCCT within 6 hours has very high sensitivity for SAH; beyond 6 hours, negative CT does not exclude SAH and CTA ± LP is required.>>
- **Pregnancy:** non-contrast head CT delivers negligible foetal dose — proceed if clinically indicated.

## 10. Take-home Messages

- HU reflects tissue composition — measure, don't guess. Tiny differences (2–5 HU) matter in early ischaemia.
- Always review bone windows and MPRs; always tailor windowing to the question.
- Know how blood evolves: hyperacute can be only 30–50 HU; subacute SDH can be isodense.
- Distinguish iodine from haemorrhage post-intervention using dual-energy or 24-hour follow-up.
- Pseudo-SAH (~30–40 HU) is not true SAH (>50 HU).
- In stroke, pair NCCT with ASPECTS, CTA, and CTP to drive