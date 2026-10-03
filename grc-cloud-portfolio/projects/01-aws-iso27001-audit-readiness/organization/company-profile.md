# Fictional Company Profile — AsterCloud Learning Ltd.

AsterCloud Learning Ltd. is a fictional cloud-native SaaS provider serving universities and professional training organizations.

## Business model

- Subscription-based web platform
- Customer administrators manage learners and courses
- Users authenticate through email/password and optional SSO
- Customer data is processed in AWS
- Engineering uses Git-based CI/CD

## Technology environment

- AWS Organizations with production and non-production accounts
- Amazon EKS for application workloads
- Amazon RDS PostgreSQL for transactional data
- Amazon S3 for documents and media
- Amazon CloudFront and AWS WAF for edge protection
- AWS IAM Identity Center for workforce access
- AWS CloudTrail, CloudWatch, Config, GuardDuty, and Security Hub for monitoring
- GitHub for source control and CI/CD

## Information handled

- customer contact details
- learner profile information
- authentication metadata
- course activity records
- support tickets
- internal operational and security logs

## Business priorities

1. Protect customer and learner information.
2. Maintain platform availability.
3. Detect unauthorized activity quickly.
4. Demonstrate consistent control operation to customers and auditors.
5. Reduce manual evidence collection through automation.
