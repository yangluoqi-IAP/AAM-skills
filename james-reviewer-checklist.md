# JAMES Reviewer Checklist

Use this reference for reviewer-style critique, self-review, and final revision planning.

## Major-Risk Findings

Flag these as high severity:

- The paper's novelty is only "uses a new neural network" without Earth-system modeling insight.
- The test split leaks information across time, station, terrain, event, or lead time.
- Baselines are too weak or missing operationally relevant comparators.
- Results are reported only as aggregate RMSE/MAE/R2 with no regime, physical, or uncertainty diagnosis.
- Generalization is claimed without independent sites, years, weather regimes, or model configurations.
- The method is called physically consistent without conservation, profile, spectrum, flow-balance, monotonicity, or case-study evidence.
- Training data, code, model weights, or configuration details are unavailable without a defensible reason.
- The conclusion overstates operational readiness.

## Baseline Adequacy

For low-altitude wind forecasting or rapid wind-field prediction, expect some combination of:

- Persistence and climatology.
- Classical statistical/ML models such as linear regression, random forest, gradient boosting, LSTM/GRU, ConvLSTM, U-Net, graph neural net, or transformer baseline as appropriate.
- NWP/WRF/HRRR/ERA5-derived forecast or analysis baseline when available.
- Ablations of key architecture modules and inputs.
- Physics-informed or terrain-aware alternatives if the manuscript claims those benefits.

If only one baseline exists, require a clear justification.

## Evaluation Completeness

Check whether the manuscript reports:

- Lead-time-dependent errors.
- Height-dependent or vertical-profile errors for low-altitude wind.
- Site/station leave-out or region transfer.
- Seasonal and diurnal variation.
- Terrain/land-cover/topographic-regime variation.
- Stable/unstable boundary-layer or weather-regime variation where data permit.
- Strong-wind, ramp, and extreme-event performance.
- Statistical uncertainty: confidence intervals, bootstrap, paired tests, or event-count caveats.
- Computational cost: training cost, inference latency, hardware, model size.

## Reproducibility

The manuscript should specify:

- Data sources, time period, spatial/temporal resolution, units, coordinates, quality-control rules.
- Exact train/validation/test split and whether it is chronological, spatial, or leave-one-site-out.
- Input features and preprocessing.
- Architecture, hyperparameters, loss function, optimizer, random seeds when possible.
- Evaluation scripts or enough metric definitions to reproduce the results.
- Code/software archive and data availability statement.

## Interpretation

For AI models, ask whether the interpretation is scientifically meaningful:

- Does the model's error pattern align with boundary-layer, terrain, or synoptic processes?
- Are difficult cases diagnosed rather than merely shown?
- Are learned features or sensitivities connected to known meteorological controls?
- Are maps/profiles/spectra physically plausible?
- Are failure modes used to define the model's domain of applicability?

## Decision-Oriented Audit Output

When auditing a manuscript, return:

1. **Major concerns**: risks that can block acceptance.
2. **Moderate concerns**: issues likely to trigger revision.
3. **Minor issues**: wording, organization, or reporting improvements.
4. **Revision priorities**: the smallest set of changes that most improves JAMES fit.

Lead with findings, not praise. Use file/section/paragraph references when available.
