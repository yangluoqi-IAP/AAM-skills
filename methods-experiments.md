# Methods And Experiments

Use this reference for Data, Method, Model Description, Experimental Design, and Evaluation sections.

## Data Section Requirements

Specify:

- Data source names and versions.
- Variables, units, height levels, temporal resolution, spatial resolution, coordinates, and time period.
- Station/site metadata, terrain class, land cover, sensor type, and quality-control procedures.
- Missing-data handling and filtering rules.
- Train/validation/test split with exact dates/sites and leakage prevention.
- Whether predictors would be available at forecast initialization in a real forecast cycle.

For low-altitude wind, include wind-speed and wind-direction treatment, vector component conversion, calm-wind thresholds, and vertical alignment across sensors.

## Method Section Requirements

Explain the modeling system, not only the neural architecture:

- Inputs and outputs.
- Forecast horizon and update frequency.
- Architecture modules and why they match the data geometry.
- Loss function and whether it targets speed, direction, vector components, extremes, or probabilistic outputs.
- Physical constraints or physically motivated features.
- Training protocol, hyperparameters, random seeds, early stopping, model selection.
- Inference latency and hardware when "rapid" or "operational" is part of the claim.

## Experiment Design

Organize experiments around claims:

- **Overall skill**: compare against persistence, climatology, NWP, statistical, and neural baselines.
- **Generalization**: independent time, leave-one-site-out, leave-one-region-out, unseen terrain, unseen season.
- **Ablation**: remove terrain, NWP predictors, upstream stations, vertical coupling, attention/graph/physics modules.
- **Regime analysis**: lead time, height, stability, diurnal cycle, terrain, wind-speed bins, extreme/ramp events.
- **Uncertainty**: prediction intervals, ensemble calibration, spread-skill, reliability diagrams if relevant.
- **Cost**: training/inference cost and forecast-cycle feasibility.

## Metrics

Use metrics matched to wind:

- RMSE, MAE, bias for speed and u/v components.
- Direction error with circular statistics or careful handling near calm winds.
- Vector RMSE where appropriate.
- Correlation and anomaly correlation only with caution.
- Threshold/event metrics for strong winds, ramps, gusts, or hazardous conditions.
- CRPS, reliability, Brier score, rank histogram, spread-skill for probabilistic forecasts.

Do not rely on R2 alone.

## Statistical Support

Use paired tests or resampling when comparing models:

- Bootstrap by time block, day, event, station, or case depending on dependence.
- Report confidence intervals for skill differences where possible.
- Keep event-count caveats visible for extremes.

## Reproducibility Wording

Methods should allow another group to reconstruct:

- Dataset construction.
- Model architecture and training.
- Evaluation split.
- Baseline implementation.
- Figure/table values.

If code/data cannot be fully public, state what is archived and why restrictions apply.
