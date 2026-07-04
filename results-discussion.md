# Results, Discussion, And Conclusions

Use this reference when revising Results, Discussion, or Conclusions.

## Results Order

Use a diagnostic progression:

1. Overall forecast skill against baselines.
2. Skill as a function of lead time and height.
3. Spatial, site, terrain, or regime generalization.
4. Event or difficult-case performance.
5. Ablation and predictor/module contribution.
6. Physical diagnostics and interpretation.
7. Uncertainty/calibration and computational cost when relevant.

Lead each subsection with the claim it tests. Do not start with figure description.

## Results Paragraph Pattern

Use this structure:

1. Result claim.
2. Evidence with metric, comparator, and domain.
3. Regime or uncertainty caveat.
4. Physical or methodological interpretation.

Example shape:

"The forecasting system provides the largest gain at intermediate lead times. Relative to persistence, RMSE decreases most strongly between 20 and 40 min, whereas the gain narrows at 5 min and after 60 min. This pattern indicates that the model adds value after persistence loses memory but before synoptic-scale predictor errors dominate."

## Discussion Tasks

The Discussion should answer:

- Why does the method improve or fail under specific regimes?
- What do the results imply for Earth-system modeling, not just this data set?
- How do the findings compare with NWP, postprocessing, downscaling, or previous ML studies?
- What are the limitations in observations, terrain coverage, lead time, physics, uncertainty, and reproducibility?
- What is the next modeling step?

## Physical Interpretation

For low-altitude wind, connect results to:

- Boundary-layer stability and diurnal mixing.
- Terrain channeling, slope/valley flows, roughness transitions.
- Synoptic forcing versus local circulations.
- Vertical shear and profile structure.
- Observation representativeness and sensor height.
- NWP surface-layer or terrain-representation biases.

## Conclusions

Use a bounded conclusion:

- Restate the contribution without hype.
- Report the strongest evidence.
- State the main scientific or operational implication.
- Name the principal limitation.
- End with a next-step direction tied to modeling, data, or deployment.

Avoid ending with generic "future work will improve the model." Be specific.

## Common Repairs

- Convert figure-by-figure narration into claim-driven subsections.
- Move implementation details out of Results and into Methods.
- Move speculative claims from Results into Discussion with hedging.
- Add limitations before reviewers have to infer them.
- Remove claims not supported by a figure, table, or stated analysis.
