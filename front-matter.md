# Front Matter

Use this reference when drafting or revising a JAMES title, Key Points, Abstract, or Plain Language Summary.

## Title

Make the title specific to the Earth-system contribution:

- Include the target variable or process: wind speed, wind vector, boundary-layer profile, downscaling, uncertainty, data assimilation.
- Include the method class only when it is central: neural weather model, diffusion model, hybrid physics-ML system, graph neural network.
- Include the domain when it matters: low-altitude, near-surface, complex terrain, subseasonal, tower network, UAS observations.

Avoid titles that are only model names plus broad claims. A JAMES title should let a reader infer the modeling problem.

## Key Points

Write three short, evidence-bearing points. Use one sentence per point.

Recommended order:

1. **What was built or evaluated**: method, data, forecast setting.
2. **What it improves**: skill, uncertainty, calibration, generalization, computational cost.
3. **Why it matters physically or operationally**: regime behavior, boundary-layer insight, transferability, reproducibility, decision relevance.

Good shape:

- "A terrain-aware neural forecasting system predicts 10-300 m wind profiles from tower observations, NWP predictors, and topographic features."
- "The model improves lead-time-dependent wind-speed and wind-direction skill relative to persistence and WRF-based baselines, especially during nocturnal stable conditions."
- "Leave-one-site-out and regime-stratified tests identify where rapid neural inference is reliable and where terrain-transition flows remain challenging."

Avoid:

- "A new model is proposed."
- "The model performs better than other methods."
- "The method has broad application prospects."

## Abstract

Use a five-move abstract:

1. **Problem**: the Earth-system or operational modeling limitation.
2. **Gap**: why existing models, observations, or ML methods are insufficient.
3. **Approach**: data, model/system, forecast target, domain, lead times.
4. **Evidence**: baselines, metrics, generalization, regimes, uncertainty, latency.
5. **Implication and boundary**: what the results enable and where they are limited.

Keep the abstract technical but readable. Do not start with generic AI enthusiasm. Put the main quantitative evidence in the abstract when available.

## Plain Language Summary

Write for scientifically interested non-specialists:

- First sentence: why the weather/climate/environmental problem matters.
- Middle: what is hard about the problem in ordinary language.
- Method: explain the model as a forecasting or correction system, not as jargon.
- Result: state the main practical finding.
- Boundary: mention where more testing is needed when relevant.

Avoid acronyms unless defined. Avoid equations, architecture jargon, and unexplained metric names.

## Common Repairs

- If Key Points read like an outline, rewrite them as findings.
- If the abstract lacks baselines, add them before polishing.
- If the Plain Language Summary repeats the abstract with simpler words, add societal or operational relevance.
- If title claims "real-time", require latency evidence and data-arrival assumptions.
