# Examples

This document contains example queries and use cases for the Google Agent Development Kit (ADK) with Ollama.

## CKM Multi-Agent Board Examples

The CKM (Cardio-Kidney-Metabolic) multi-agent board uses a specialized pattern where three specialist agents (cardiologist, nephrologist, and diabetologist) assess cases in parallel, followed by a mediator agent that synthesizes their recommendations.

### Example 1: Free-Form Text Case

**Patient Case:**

```
65-year-old male with:
- Type 2 diabetes (HbA1c 8.2%)
- Chronic kidney disease Stage 3a (eGFR 58 mL/min/1.73m², creatinine 1.4 mg/dL)
- Heart failure with reduced ejection fraction (EF 35%, BNP 450 pg/mL)
- Current medications: metformin 1000mg BID, lisinopril 10mg daily, metoprolol 50mg BID
- BP: 142/88 mmHg, HR: 78 bpm
- Chief complaint: Increasing fatigue and shortness of breath over past 2 weeks
```

**Expected Behavior:**

The root agent will delegate this case to the CKM board, which will:

1. Run three specialist agents in parallel:

   - Cardiologist: Assesses heart failure management
   - Nephrologist: Evaluates kidney function and CKD staging
   - Diabetologist: Reviews diabetes management and glycemic control
1. Mediator agent synthesizes the three assessments into a unified treatment plan

**Expected Output:**

A comprehensive narrative summary that includes:

- Summary of the case and key findings
- Areas of agreement between specialists
- Any conflicts and their resolutions
- Prioritized action plan
- Medication recommendations
- Monitoring plan
- Follow-up recommendations

---

### Example 2: Structured Free-Form Text Case

**Patient Case:**

```
72-year-old female patient

Demographics:
- Age: 72 years
- Sex: Female
- Weight: 85 kg
- Height: 165 cm

Medical History:
- Type 2 diabetes, diagnosed 2015
- Essential hypertension
- CKD Stage 3b

Vital Signs:
- Blood pressure: 138/82 mmHg
- Heart rate: 82 bpm

Laboratory Results:
- HbA1c: 7.8%
- eGFR: 45 mL/min/1.73m²
- Creatinine: 1.6 mg/dL
- Glucose: 165 mg/dL
- Ejection fraction: 42%
- NT-proBNP: 320 pg/mL

Current Medications:
- Metformin 500mg BID
- Glipizide 5mg daily
- Losartan 50mg daily

Chief Complaint:
Progressive lower extremity edema and weight gain of 5kg over 1 month
```

**Expected Behavior:**

Same as Example 1 - the root agent processes this free-form text case through the CKM multi-agent board pattern, with all three specialists providing parallel assessments followed by mediator synthesis.

**Expected Output:**

A comprehensive narrative summary with unified treatment recommendations from all three specialists.

---

## Usage Notes

- All examples use the Ollama `ministral-3:14b` model
- The CKM board examples demonstrate the multi-agent pattern where specialists work in parallel
- All input should be provided as free-form text (no JSON required)
- Output is provided as narrative text summaries optimized for clinical review