# Day 1 — Portfolio Build Plan

Do not try to finish the entire project today. The goal is to produce a credible first commit and understand every artifact you publish.

## Today — 60 to 90 minutes

### 1. Read the fictional company scenario
- `organization/company-profile.md`
- `organization/scope.md`

### 2. Review the asset register
Open `assets/asset-register.csv` and challenge every row.

For at least three assets, answer:
- Why is this criticality appropriate?
- Does it contain PII?
- Is it internet exposed directly or indirectly?
- What are realistic RTO/RPO values?

### 3. Review one risk deeply
Start with `RSK-003` — security events not detected or investigated.

Write a short note answering:
- Why is inherent likelihood 4?
- Why is inherent impact 4?
- What controls reduce likelihood?
- What evidence would prove those controls operate over time?
- Why should residual risk remain 12 while alert-review evidence is incomplete?

### 4. Test one control
Use `audit/control-test-template.md` for `LOG-001`.

Your objective is to distinguish:
- design effectiveness
- implementation
- operating effectiveness

### 5. Run the GRC-as-Code validator

```bash
cd projects/01-aws-iso27001-audit-readiness
python -m pip install -r automation/requirements.txt
python automation/validate_controls.py
```

Expected output:

```text
GRC control validation PASSED: 7 controls checked
```

### 6. Make your first Git commit

Suggested commit message:

```text
feat: initialize AWS ISO 27001 audit readiness lab
```

## Do not publish yet

Before making the repository public, remove anything that came from a real employer or client. This project must remain entirely fictional.
