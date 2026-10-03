# ISMS / Audit Readiness Scope

## Proposed scope

The audit-readiness scope covers the design, development, operation, monitoring, and support of the AsterCloud SaaS platform, including production AWS infrastructure, supporting cloud security services, CI/CD processes, workforce administrative access, and operational processes that materially affect confidentiality, integrity, and availability.

## In scope

- AWS production account(s)
- AWS shared security/logging services
- EKS application platform
- RDS databases
- S3 data stores
- IAM / workforce access
- CloudTrail / Config / GuardDuty / Security Hub
- GitHub CI/CD workflows relevant to production
- change management
- incident management
- backup and recovery
- vulnerability management
- access reviews

## Initially out of scope

- employee personal devices except where they provide privileged administrative access
- customer-owned endpoints
- third-party systems that do not process or protect scoped information

## TODO

- [ ] Define exact legal entity and locations.
- [ ] Identify interested parties.
- [ ] Identify contractual/regulatory obligations.
- [ ] Define boundaries for corporate IT and SaaS tools.
