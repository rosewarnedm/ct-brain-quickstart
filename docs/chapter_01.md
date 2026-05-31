---
layout: default
title: "Chapter 01: CT Physics and Technique"
nav_order: 1
---

# CT Physics and Technique for Acute Brain CT
## Practical Guide for ED Physicians and Junior Radiologists

---

## 1. Why Physics Matters at the Workstation

CT images are numerical: every pixel carries a Hounsfield Unit (HU) value representing how much that tissue attenuates X-rays compared with water. <mark>HU = 1000 × (μ_tissue − μ_water) / μ_water.</mark> Recognising pathology on brain CT is fundamentally about recognising abnormal HU values and the patterns they create. Getting the technique right — slice thickness, windows, reconstruction — determines whether you can see a 3 HU difference that represents early infarction, or a thin subdural that changes your management.

---

## 2. Normal HU Values You Must Know

These are approximate values at 120 kVp on a standard brain kernel:

| Tissue | HU Range |
|---|---|
| Air | −1000 |
| Fat | −80 to −120 |
| CSF | ~0 to +15 |
| White matter | +20 to +30 |
| Grey matter | +35 to +45 |
| Acute clotted blood | +60 to +80 (range +50 to +90) |
| Cortical bone | +1000 to +2000 |

<mark>HU values depend on acquisition parameters (kVp, kernel) and differ between scanners — always compare to an internal reference (contralateral hemisphere, blood pool) rather than relying on absolute numbers alone.</mark>

**Key rule:** Grey matter is normally ~10 HU brighter than white matter. Loss of this differential is the hallmark of early ischaemia.

---

## 3. Acquisition Parameters That Directly Affect What You See

### Tube Voltage and Current
- <mark>Routine non-contrast CT (NCCT) brain: use 120 kVp.</mark>
- <mark>CTA/CTV: use 80–100 kVp</mark> to exploit iodine's photoelectric effect, boosting contrast conspicuity.
- Tube current (mAs) is usually controlled by automatic exposure control (AEC). <mark>Typical adult NCCT: effective mAs ~200–350; CTDIvol ~45–65 mGy.</mark>
- Lower mAs = more noise; thinner slices = more noise. You cannot have everything simultaneously.

### Slice Thickness for Reconstruction
This is the single most important technical choice after the scan is acquired:
- <mark>Standard review: 3–5 mm axial slices.</mark>
- <mark>ASPECTS scoring and stroke assessment: reconstruct at 2–2.5 mm.</mark>
- <mark>Thin subdural and trauma: review ≤1 mm axial and coronal MPRs.</mark>
- Coverage must include foramen magnum to vertex — do not accept a scan that cuts off the posterior fossa or high convexities.

### Gantry Tilt
- Tilt parallel to the skull base (orbito-meatal line) to reduce beam hardening in the posterior fossa and minimise lens irradiation. This is more effective than adding bismuth shielding.

---

## 4. Windowing: Seeing What Is There

The same dataset looks completely different depending on your window. Use multiple windows on every acute scan:

| Purpose | Window Level (WL) | Window Width (WW) |
|---|---|---|
| Brain parenchyma | 35–40 | 70–90 |
| Stroke/grey–white | 30–35 | 25–40 |
| Subarachnoid blood | 50–60 | 100–140 |
| Bone | 300–500 | 2000–3000 |

<mark>The "stroke window" (WL ~30–35, WW ~25–40) is essential to detect the 2–5 HU drop of early cytotoxic oedema — this change is invisible on standard brain windows.</mark>

Always compare left and right on the same window, and confirm with MPRs before calling subtle findings.

---

## 5. Blood on CT: Recognition and Evolution

### Acute Haemorrhage
<mark>Acute clotted haemorrhage: typically +60 to +80 HU</mark> (clot retraction concentrates haemoglobin). This makes it bright (hyperdense) against grey matter (+35–45 HU) and white matter (+20–30 HU).

### Evolution Over Time
- <mark>Days 3–7: haemoglobin breakdown causes progressive HU fall; haematoma may become isoattenuating to brain (~30–40 HU) and difficult to detect.</mark>
- <mark>>3 weeks: chronic haematoma becomes hypodense, approaching CSF density (0–20 HU).</mark>

**Clinical implication:** A subacute haematoma can be completely invisible on NCCT. If clinical history suggests a bleed at 5–10 days, look for subtle mass effect, surrounding oedema, or a thin rim — and consider MRI.

### Subarachnoid Haemorrhage (SAH)
- Acute SAH: hyperdense blood fills basal cisterns and sulci; <mark>typically >50 HU</mark>.
- Clears over 3–7 days — a normal CT does not exclude SAH after 6 hours.
- Intraventricular blood layers dependently.

### Dural Venous Sinus Thrombosis (DVST)
- <mark>Acute thrombus in a dural sinus: typically >60–70 HU</mark>.
- Dehydration and polycythaemia also raise venous density — use the sinus HU/haematocrit ratio or confirm with CTV/MRV.

---

## 6. Early Ischaemia: The Subtle Signs

<mark>Early cytotoxic oedema produces only a 2–5 HU drop in the affected tissue.</mark> This is why you need stroke windows, thin slices, and side-to-side comparison. Look for:

1. **Loss of insular ribbon** — insular cortex approaches white matter density (grey–white contrast lost).
2. **Lentiform nucleus obscuration** — basal ganglia normally very clearly defined; early ischaemia makes them less distinct.
3. **Cortical hypoattenuation with sulcal effacement** — in an arterial territory distribution.
4. **Hyperdense artery sign** — acute thrombus within an artery appears brighter than flowing blood. <mark>Flowing blood: ~30–45 HU; MCA thrombus: ~55–70 HU. An MCA HU >43–45 suggests thrombus on most scanners; HU:blood pool ratio >1.2–1.5 increases specificity.</mark>

**Calcified artery mimicking hyperdense MCA:** Check bone windows — calcification is extremely dense (often >200 HU) with crisp edges; the hyperdense MCA sign due to thrombus is less extreme and usually unilateral.

<mark>ASPECTS should be scored on ≤2.5 mm reconstructions using stroke windows</mark> to detect all 10 regions reliably. This directly informs thrombolysis and thrombectomy decisions.

---

## 7. Artefacts: The Major Causes of Error

### Beam Hardening (Posterior Fossa)
- **Appearance:** Dark bands across the brainstem/cerebellum.
- **Pitfall:** Easily mistaken for infarction.
- **Fix:** Check coronal and sagittal MPRs — true infarction maintains its appearance on reformats; beam hardening changes character. Use high-keV monoenergetic images if dual-energy available. Correlate clinically.

### Motion
- **Appearance:** Blurring, double edges, indistinct sulci.
- **Pitfall:** Mimics effacement, obscures haemorrhage.
- **Fix:** Immobilise, use fast rotation times; repeat if severely degraded.

### Partial Volume Averaging
- **Appearance:** Thin subdurals and cortical SAH invisible on 5 mm slices.
- **Fix:** <mark>Always review ≤1 mm axial and coronal MPRs along the convexities and interhemispheric fissure when thin extra-axial blood is suspected.</mark>

### Dental and Metal Streaks
- **Appearance:** Starburst streaks, photon starvation artefact.
- **Fix:** Metal artefact reduction (MAR) algorithms, high-keV monoenergetic images (dual-energy), gantry angle adjustment.

### Out-of-Field Artefact
- Off-centre positioning causes geometric distortion and peripheral bright/dark banding. Ensure proper centring.

---

## 8. Contrast CT Techniques

### CT Angiography (CTA)
**When:** Suspected large vessel occlusion (LVO), aneurysm, dissection, traumatic vascular injury.

- <mark>kVp: 80–100 in average-sized adults; 100–120 kVp in large patients.</mark>
- <mark>Contrast: 50–80 mL at 4–6 mL/s via 18–20G antecubital access; 30–50 mL saline chaser.</mark>
- <mark>Timing: bolus-track in ascending aorta or carotid, trigger at ~120 HU.</mark>
- Coverage from aortic arch to vertex when stroke/tandem occlusion is suspected.
- Reconstruct at <mark>0.5–0.75 mm</mark> for MIP/MPR/VR.

**Pitfalls:**
- Late timing → venous contamination mimics absent sinus.
- Calcium blooms → exaggerates stenosis (use thin slices, 70–80 keV virtual monoenergetic).
- Slow flow → mimics occlusion; correlate with contralateral side and consider multiphase CTA.

### CT Venography (CTV)
**When:** Suspected DVST.
- Delayed phase 45–70 s after CTA contrast injection, or dedicated venous phase.
- <mark>80–100 kVp; thin slices; coronal and sagittal MIP.</mark>
- Pitfall: Hypoplastic transverse sinus vs thrombus; arachnoid granulations (round filling defects with CSF density — not thrombus).

### CT Perfusion (CTP)
**When:** Acute stroke triage, especially late window (>6 hours or wake-up stroke).
- Produces maps of CBF, CBV, and Tmax/MTT.
- <mark>Core infarct: typically defined as very low CBF (<30% of contralateral) with reduced CBV.</mark>
- <mark>Penumbra: prolonged Tmax (>6 s) with relatively preserved CBV.</mark>
- <mark>Coverage is limited (typically 4–16 cm z-axis) — truncation can underestimate infarct volume.</mark>
- **Pitfalls:** Motion corrupts maps; old infarcts and leukoaraiosis inflate apparent penumbra; post-recanalisation contrast staining mimics haemorrhage on NCCT (dual-energy distinguishes iodine from blood).

---

## 9. Dual-Energy CT: When to Use It

Dual-energy CT acquires data at two X-ray energies simultaneously, enabling material decomposition.

**Key applications in neuroemergency:**
- **Iodine vs haemorrhage:** Virtual non-contrast (VNC) images subtract iodine — hyperdensity that disappears on VNC is iodine (contrast staining); residual hyperdensity is blood. Critical after thrombectomy when contrast staining vs haemorrhage changes anticoagulation decisions.
- **Metal/dental artefact reduction:** High-keV (90–130 keV) monoenergetic images dramatically reduce streaks.
- **CTA:** Low-keV (50–70 keV) images boost iodine conspicuity and improve aneurysm detection.

<mark>VNC is not identical to true NCCT — small haemorrhages can be obscured by residual iodine signal. Do not rely on VNC alone when small haemorrhage is clinically critical.</mark>

---

## 10. Critical Mimics and Pitfalls

### Pseudo-SAH
- **Context:** Severe diffuse cerebral oedema (post-cardiac arrest, raised ICP).
- **Mechanism:** Engorged pial veins appear hyperdense against the abnormally low-density swollen brain.
- <mark>Measured HU in pseudo-SAH is typically ~30–40 HU — lower than true SAH (>50 HU).</mark>
- Clues: globally low brain attenuation, absent sulci, narrow ventricles, no dependent intraventricular layering.
- **Management:** Do not trigger aneurysm work-up based on this appearance alone; integrate clinical context.

### Contrast Staining vs Haemorrhage Post-Thrombectomy
- Iodine extravasation is hyperdense acutely but washes out on a delayed scan (~24 hours) or subtracts on dual-energy VNC.
- <mark>This distinction is clinically critical: haemorrhagic transformation may contraindicate antiplatelet/anticoagulant therapy; contrast staining does not.</mark>

### Calcification vs Haemorrhage
- Physiological calcifications (choroid plexus, pineal, falx, basal ganglia): <mark>very high HU, often >100–200 HU</mark>, crisp margins on bone kernel, bilateral/symmetric, stable over time.
- Dual-energy material decomposition can confirm calcium.

### Posterior Fossa "Infarct"
- Beam hardening is the most common cause of apparent brainstem/cerebellar hypodensity.
- Confirm on coronal/sagittal MPRs; use high-keV monoenergetic images; correlate clinically. If in doubt, MRI.

### Thin Subdural Haematoma
- <mark>Missed on 5 mm slices due to partial volume averaging — mandatory review of ≤1 mm coronal MPRs along convexities and interhemispheric fissure.</mark>

---

## 11. When to Escalate

| Situation | Action |
|---|---|
| NCCT normal but SAH clinically suspected (>6 h from ictus) | LP and/or MRI (FLAIR/GRE/SWI) |
| Subacute haematoma suspected (5–14 days, isoattenuating) | MRI |
| CTA equivocal for aneurysm | DSA or MRA |
| Post-thrombectomy hyperdensity: iodine vs blood uncertain | Dual-energy CT or delayed NCCT at 24 h |
| Posterior fossa hypodensity — artefact vs infarct | MRI DWI |
| ASPECTS ≤5 or major early ischaemic change | Senior/neuroradiology review immediately |

---

## 12. Systematic Reading Checklist for Acute Brain CT

1. **Check protocol:** <mark>Stroke: ≤2.5 mm slices; coronal MPRs obtained; stroke window applied.</mark>
2. **Grey–white differentiation:** Apply stroke window; compare hemispheres.
3. **Hyperdense artery sign:** Quantify HU; confirm with CTA if present.
4. **Basal cisterns and sulci:** SAH vs pseudo-SAH; adjust window; check HU.
5. **Posterior fossa:** Review on MPRs; assume artefact until disproved.
6. **Extra-axial spaces:** Thin-slice coronal MPRs — never just 5 mm axials.
7. **Ventricles:** Intraventricular blood; hydrocephalus.
8. **Skull/skull base (trauma):** Bone kernel; coronal MPRs.
9. **Cross-check findings against technique artefacts** before finalising.
10. **Escalate** when uncertainty affects a time-critical management decision.

---

## Self-assessment MCQs

**Q1.** A 67-year-old man presents with sudden onset left-sided weakness and dysarthria. NCCT is performed at 120 kVp with 5 mm reconstructions. You apply a standard brain window (WL 40, WW 80) and the scan appears normal. A colleague suggests reviewing with a stroke window. Which window settings should you apply to best detect early cytotoxic oedema?

A. WL 80, WW 200  
B. WL 50, WW 120  
C. WL 30, WW 30  
D. WL 400, WW 2000  
E. WL 0, WW 50  

---

**Q2.** You are reviewing an NCCT following out-of-hospital cardiac arrest and successful resuscitation. The basal cisterns appear hyperdense, raising concern for subarachnoid haemorrhage. You measure the HU in the region of apparent hyperdensity and obtain a value of 34 HU. The brain parenchyma appears globally hypoattenuating and the sulci are effaced. What is the most likely explanation?

A. Aneurysmal subarachnoid haemorrhage requiring urgent CTA  
B. Traumatic subarachnoid haemorrhage from the resuscitation  
C. Pseudo-subarachnoid haemorrhage due to diffuse cerebral oedema  
D. Intrathecal contrast from recent lumbar puncture  
E. Dural venous sinus thrombosis with venous infarction  

---

**Q3.** A 52-year-old woman with sudden severe headache undergoes NCCT at 8 hours after symptom onset. The scan appears normal. Which of the following represents the most appropriate next step?

A. Discharge with reassurance as NCCT sensitivity for SAH is >99% at all time points  
B. CT angiography to look for an aneurysm as the scan is diagnostic of non-aneurysmal SAH  
C. Lumbar puncture and/or MRI, as NCCT sensitivity for SAH declines significantly after 6 hours  
D. Repeat NCCT in 24 hours using a stroke protocol  
E. No further imaging as the clinical probability of SAH is low if NCCT is normal  

---

**Q4.** During review of a post-thrombectomy NCCT, you identify new hyperdensity in the right MCA territory. You need to determine whether this represents haemorrhagic transformation or contrast staining, as antiplatelet therapy is being considered. Which of the following is the most appropriate next imaging step?

A. Repeat NCCT at 120 kVp immediately with a bone kernel  
B. MRI with gradient echo sequence  
C. Dual-energy CT with virtual non-contrast reconstruction, or delayed NCCT at 24 hours  
D. CT perfusion to assess residual penumbra  
E. CTA to assess vessel patency  

---

**Q5.** A 44-year-old man is imaged following head trauma. The 5 mm axial NCCT images are reported as normal. However, his GCS remains depressed. Which additional review would most likely identify a missed thin subdural haematoma?

A. Repeat NCCT with intravenous contrast  
B. Review of 1 mm coronal MPR reconstructions windowed for soft tissue along the convexities and interhemispheric fissure  
C. PET-CT to assess metabolic activity  
D. Nuclear medicine brain perfusion scan  
E. Review the existing images with a bone window only  

---

### Answers

**Q1. C — WL 30, WW 30**
The narrow stroke window (WL ~30–35, WW ~25–40) compresses the displayed HU range so that a 2–5 HU difference between normal and ischaemic tissue becomes visible; this change is undetectable on standard brain windows.
- A: Too high a level and too wide a width — will not display the grey–white interface optimally.
- B: Closer to a subarachnoid haemorrhage window — useful for SAH detection but not optimal for subtle grey–white loss.
- D: A bone window — appropriate for skull but renders soft tissue structures indistinguishable.
- E: Centred at 0 HU (CSF level) — would make grey and white matter look similarly bright and obscure the relevant differential.

**Q2. C — Pseudo-subarachnoid haemorrhage due to diffuse cerebral oedema**
The measured HU of 34 HU is below the typical threshold for true SAH (>50 HU); the combination of globally hypoattenuating parenchyma and effaced sulci points to severe diffuse oedema creating a contrast effect rather than genuine subarachnoid blood.
- A: True aneurysmal SAH would typically measure >50 HU in the cisterns; triggering CTA on this basis risks anchoring on a false finding.
- B: Traumatic SAH from resuscitation alone would be very unusual and would not explain the globally low brain attenuation.
- D: Intrathecal contrast would require a recent procedure and would measure much higher HU; clinical history distinguishes this.
- E: DVST can cause venous infarction and haemorrhage but would not produce this specific global pattern with the measured HU of 34.

**Q3. C — Lumbar puncture and/or MRI, as NCCT sensitivity for SAH declines significantly after 6 hours**
NCCT sensitivity for SAH, whilst very high in the first 6 hours (approaching 98–100%), falls substantially thereafter as blood is diluted and cleared; a normal scan at 8 hours does not exclude SAH and further investigation is mandatory in a patient with thunderclap headache.
- A: Incorrectly states NCCT sensitivity is >99% at all time points — this is only true in the hyperacute period.
- B: A normal NCCT cannot diagnose "non-aneurysmal SAH" — SAH has not been confirmed.
- D: Repeating NCCT in 24 hours would further delay diagnosis and sensitivity would be even lower.
- E: A normal NCCT at 8 hours should lower suspicion but does not exclude SAH — thunderclap headache mandates further investigation regardless.

**Q4. C — Dual-energy CT with virtual non-contrast reconstruction, or delayed NCCT at 24 hours**
Iodine extravasation (contrast staining) subtracts on VNC images and washes out on a delayed NCCT, whereas haemorrhage persists; this distinction directly informs the safety of antiplatelet/anticoagulant therapy after thrombectomy.
- A: Repeat NCCT at the same energy with a bone kernel does not distinguish iodine from blood.
- B: MRI gradient echo is valuable for haemorrhage detection but is less immediately practical in the acute thrombectomy setting and does not directly distinguish contrast from blood in this context as reliably as dual-energy.
- D: CT perfusion assesses ischaemia, not haemorrhage composition.
- E: CTA assesses vessel patency — important but does not resolve the haemorrhage vs contrast question.

**Q5. B — Review of 1 mm coronal MPR reconstructions windowed for soft tissue along the convexities and interhemispheric fissure**
Thin subdural haematomas are frequently invisible on 5 mm axial images due to partial volume averaging; 1 mm coronal MPRs along the convexities provide the optimal plane and slice thickness to detect thin extra-axial collections.
- A: Intravenous contrast is not indicated as the first step for traumatic subdural — NCCT with thin MPRs is the appropriate technique.
- C: PET-CT has no role in acute trauma assessment.
- D: Nuclear medicine perfusion scanning has no role in acute trauma.
- E: Bone windows are essential for fracture detection but will not improve visibility of a thin isodense or hyperdense subdural collection; soft tissue windows on thin coronal MPRs are required.