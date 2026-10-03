# Risk Assessment Methodology

## Scale

Likelihood and impact are scored from 1 to 5.

### Likelihood

1. Rare
2. Unlikely
3. Possible
4. Likely
5. Almost certain

Likelihood should consider exposure, threat activity, control maturity, attack surface, incident history, and detectability. It should not be selected by intuition alone.

### Impact

1. Insignificant
2. Minor
3. Moderate
4. Major
5. Severe

Impact should consider confidentiality, integrity, availability, privacy, legal/contractual obligations, financial loss, and customer impact.

## Inherent risk

`Inherent Risk = Inherent Likelihood × Inherent Impact`

Inherent risk is assessed **before** considering existing controls.

## Control effectiveness

Rate control effectiveness separately:

- 0 = Not implemented
- 1 = Weak
- 2 = Partially effective
- 3 = Effective
- 4 = Strong and evidenced over time

The effectiveness rating must be based on design, implementation, and operating evidence.

## Residual risk

Residual likelihood and impact are reassessed after considering verified control operation. Do not lower residual risk merely because a policy exists or a tool is enabled.

## Rating bands

- 1–4: Low
- 5–9: Moderate
- 10–15: High
- 16–25: Critical

## Review triggers

Reassess risk when:

- a material control fails
- an asset changes classification or exposure
- a security incident occurs
- a new threat or vulnerability materially changes likelihood
- a major architecture or supplier change occurs
