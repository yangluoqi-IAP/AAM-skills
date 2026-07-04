# JAMES Article Architecture

Use this reference to plan or restructure a full JAMES manuscript.

## Standard Flow

A strong JAMES paper usually follows this logic:

1. **Front matter**
   - Title
   - Key Points
   - Abstract
   - Plain Language Summary
2. **Introduction**
   - Earth-system problem
   - Existing modeling/data limitation
   - Specific gap in prediction, parameterization, uncertainty, or computational cost
   - Contribution and validation design
3. **Data**
   - Observations, model outputs, reanalysis/NWP products, terrain/land-surface data
   - Quality control, temporal/spatial coverage, train/validation/test split
4. **Method or Model Description**
   - Architecture or modeling system
   - Physical constraints, coupling, inputs/outputs, loss functions
   - Inference and computational setup
5. **Experiments or Evaluation Design**
   - Baselines, ablations, regimes, metrics, statistical testing
   - Generalization and robustness tests
6. **Results**
   - Overall skill
   - Regime/site/height/lead-time behavior
   - Case studies and physical diagnostics
   - Uncertainty, calibration, or failure modes if relevant
7. **Discussion**
   - Why the method works
   - What it means for Earth-system modeling or operations
   - Limitations and transferability
8. **Conclusions**
   - Bounded contribution
   - Main evidence
   - Next modeling step
9. **Open Research**
   - Data availability
   - Code/software availability
   - Configuration and trained-model access where possible

## Paper Story Spine

Use this spine before drafting:

- Problem: What low-level atmospheric process or forecast decision is limited?
- Gap: Why existing NWP, reanalysis, statistical, or ML methods are insufficient?
- Method: What modeling system, neural architecture, or hybrid workflow addresses the gap?
- Evidence: What independent tests demonstrate skill and robustness?
- Interpretation: What physical behavior explains gains or failures?
- Boundary: Where should the method be trusted, and where not yet?

## Common JAMES Section Names

Observed samples frequently use combinations of:

- Introduction
- Data
- Methods or Method
- Model Description
- Data and Optimization Process
- Experiments or Experimental Design
- Results
- Results and Discussion
- Discussion
- Discussion and Conclusions
- Conclusions
- Data Availability Statement
- Acknowledgments
- References

Choose section names that help readers find reproducible modeling details. Do not hide evaluation protocol inside Results if it affects interpretation.

## Contribution Types

For a JAMES submission, make the contribution explicit:

- **New forecasting model**: Show skill, latency, generalization, and physical diagnostics.
- **Hybrid physics-ML model**: Show coupling design, stability, balance, and comparison to host model.
- **Downscaling/bias correction**: Show cross-resolution, cross-lead-time, spatial generalization, and extremes.
- **Parameterization/emulator**: Show offline skill plus online stability and climate/weather impacts when possible.
- **Uncertainty/ensemble calibration**: Show calibration, reliability, spread-skill, rank histograms, CRPS/Brier/log score, and event performance.
- **Observation/data-assimilation study**: Show observation-error characterization, assimilation impact, and independent validation.

## Full-Paper Revision Order

1. Fix the central claim and paper title.
2. Rebuild Abstract, Key Points, and Plain Language Summary after the main evidence is settled.
3. Make Introduction end with contribution and validation design, not a generic list of aims.
4. Move all split/evaluation details into Data/Methods/Experiments.
5. Reorder Results from broad skill to diagnostic explanation.
6. Make Discussion own the limitations instead of hiding them.
7. Add Open Research details before final polishing.
