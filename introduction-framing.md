# Introduction Framing

Use this reference when drafting or revising a JAMES Introduction or contribution paragraph.

## Four-Part Introduction

1. **Earth-system need**
   - State the modeling or prediction problem in concrete terms.
   - For low-altitude wind: connect to boundary-layer dynamics, terrain, energy, transport, UAS, air quality, or operational nowcasting.
2. **Current limitation**
   - Explain why NWP, reanalysis, observations, interpolation, or existing ML are insufficient.
   - Be specific: coarse resolution, surface-layer bias, sparse vertical observations, high computational cost, poor uncertainty calibration, weak transferability.
3. **Methodological opportunity**
   - Describe why the proposed data-driven, hybrid, or neural approach is plausible for this gap.
   - Tie architecture choices to data geometry or physics, not fashion.
4. **Contribution and evidence**
   - End with what the paper does and how it proves it.
   - Mention data, baselines, split design, regimes, and main diagnostics.

## Final Paragraph Template

Use this move order:

"Here we [develop/evaluate] [method/system] for [forecast target] using [data sources]. The system [key capability]. We evaluate it against [baselines] across [validation dimensions]. The analysis focuses on [scientific/operational question], including [regime/uncertainty/physical diagnostics]."

## Related Work Handling

Do not produce a chronological list. Group prior work by function:

- NWP and physical modeling limitations.
- Statistical or MOS-style correction.
- Deep-learning weather forecasting or downscaling.
- Boundary-layer, terrain, or surface-wind studies.
- Uncertainty, calibration, or data assimilation if relevant.

For each group, write:

- What the field can already do.
- What remains unresolved for this manuscript's target.
- How the present study is positioned without overstating novelty.

## Low-Altitude Wind Framing Questions

Make the Introduction answer these:

- What exact height range and forecast horizon matter?
- Why are low-altitude winds harder than upper-air fields or 10-m-only forecasts?
- What observations or predictors make rapid forecasting feasible?
- What part of the problem is physical, statistical, computational, or operational?
- What evidence would convince a JAMES reviewer that this is not just local curve fitting?

## Failure Modes

Flag and repair:

- Motivation is only "wind affects many fields" without a modeling gap.
- Literature review lists many AI models but no Earth-system limitation.
- Contribution paragraph says "higher accuracy" but not where, against what, or why.
- The model name appears before the scientific problem.
- "Generalization" is claimed before the validation design is introduced.
