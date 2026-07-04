# JAMES Core Style

Use this reference for the default stance, tone, and manuscript priorities.

## Journal Stance

JAMES papers are not only AI demonstrations. They must read as advances in Earth-system modeling. Frame the manuscript around a modeling or prediction problem, then show how the method improves scientific or operational capability.

Emphasize:

- Model development, evaluation, coupling, parameterization, uncertainty, prediction, or computational efficiency.
- Physical and geophysical interpretation of model behavior.
- Reproducible data, code, configurations, and evaluation protocols.
- Clear limitations and domain boundaries.

Avoid:

- Generic "deep learning achieves high accuracy" framing.
- Leaderboard-style metrics without geophysical diagnosis.
- Vague "complex nonlinear relationship" language.
- Claims of generalization without independent sites, regimes, years, or lead times.

## Voice

Use a precise, evidence-led, moderately technical voice:

- "We evaluate..." when the main contribution is evidence.
- "We introduce..." when there is a genuine method or system contribution.
- "The results indicate/suggest..." when evidence is bounded.
- "This improvement is largest under..." when regime dependence matters.

Prefer concrete nouns:

- "10-m wind-speed forecasts", "low-level wind profiles", "lead-time-dependent error", "terrain-conditioned generalization", "inference latency", "station leave-out validation".

Avoid inflated phrases:

- "revolutionary", "perfect", "unprecedented" unless proven by field-wide evidence.
- "real-time" unless latency and hardware are reported.
- "physical consistency" unless a test is shown.

## Claim Discipline

Every major claim needs four parts:

1. **Object**: what variable, level, region, lead time, or process?
2. **Comparator**: compared with what baseline or prior model?
3. **Magnitude**: how large is the improvement or error?
4. **Boundary**: where does it hold or fail?

Example claim shape:

"Across lead times of 10-60 min, the model reduces tower-level wind-speed RMSE relative to persistence and WRF-based baselines, with the largest gains under terrain-transition and nocturnal-stability regimes."

## AI Paper Standard

For neural weather or wind forecasting papers, make the ML component answer at least one JAMES-level question:

- Can the method improve an Earth-system model forecast, not only interpolate observations?
- Does it generalize across space, time, terrain, height, season, or synoptic regimes?
- Does it preserve or reveal physically meaningful structure?
- Does it quantify uncertainty or failure modes?
- Does it reduce computational cost enough to matter for operational cycles?
- Can another group reproduce the training, inference, and evaluation?

## Chinese-to-English Repair

When revising Chinese-authored drafts:

- Move the main claim earlier.
- Replace broad motivation with a specific modeling gap.
- Convert "本文提出..." into a contribution plus evidence sentence.
- Replace "验证了有效性" with the exact validation protocol and metric.
- Translate "低空" contextually: "low-altitude", "low-level", "near-surface", "boundary-layer", or exact heights.
- Translate "快速预测" as "rapid forecasting" or "low-latency inference" only with a runtime or forecast-cycle constraint.

## Sentence Patterns

Use these as patterns, not templates to repeat mechanically:

- "Here we develop/evaluate a [method] for [variable/process] using [data/model], with validation across [independent dimensions]."
- "The central challenge is that [physical/data limitation], which causes [modeling consequence]."
- "Compared with [baseline], [method] improves [metric] by [amount] while preserving [physical/operational property]."
- "The method is most reliable under [regime] and degrades under [failure mode], indicating [interpretation]."
- "These results position the model as [bounded use], rather than as a replacement for [broader system]."
