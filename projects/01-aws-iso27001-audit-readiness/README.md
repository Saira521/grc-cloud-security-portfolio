# Project 01 — AWS + ISO 27001 Audit Readiness Lab

## Scenario

**AsterCloud Learning Ltd.** is a fictional SaaS company delivering a multi-tenant learning platform. Most production workloads run in AWS. The company is preparing for an ISO/IEC 27001 audit and wants to improve cloud governance, evidence quality, and continuous control monitoring.

This project is deliberately designed as an **audit-readiness package**, not a certification claim.

## Objectives

- Define an auditable ISMS/cloud scope.
- Build an AWS-focused asset inventory.
- Identify and score security risks.
- Create a unified control library with AWS implementations.
- Map controls to relevant framework requirements without reproducing copyrighted standard text.
- Test both design and operating effectiveness.
- Track evidence, findings, corrective actions, and residual risk.
- Validate control files automatically as GRC-as-Code.

## Deliverables

| Area | Artifact | Status |
|---|---|---|
| Organization | ISMS scope | Starter complete |
| Assets | Asset register | Starter dataset included |
| Risks | Risk methodology | Starter complete |
| Risks | Risk register | Starter dataset included |
| Controls | Unified control library | Starter controls included |
| Controls | Framework mapping | TODO |
| Audit | Evidence register | Starter dataset included |
| Audit | Control test worksheet | Starter included |
| Findings | Findings register | Starter included |
| Remediation | Corrective action tracker | Starter included |
| Automation | YAML validator | Included |
| Automation | GitHub Actions workflow | Included |

## How to use this project

Treat this as a real engagement. Do not fill every row at once.

1. Read `organization/company-profile.md` and `organization/scope.md`.
2. Review the asset register and classify each asset.
3. Read the risk methodology and complete the risk register.
4. Review each control in `controls/unified-controls.yaml`.
5. Add framework references using your authorized/licensed copies of applicable standards.
6. Test controls using `audit/control-test-template.md`.
7. Record evidence in `audit/evidence-register.csv`.
8. Raise findings where operating evidence is insufficient.
9. Update residual risk only after evaluating control effectiveness.
10. Run `python automation/validate_controls.py`.

## What this demonstrates to recruiters

- practical GRC execution
- AWS/cloud governance understanding
- evidence-based audit readiness
- risk scoring discipline
- control ownership and traceability
- structured compliance automation
- Git-based governance workflows
