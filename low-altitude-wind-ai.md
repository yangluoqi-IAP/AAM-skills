# Low-Altitude Wind AI Manuscripts

Use this reference for deep-learning rapid forecasting of low-altitude or low-level wind fields.

## Core Framing

A JAMES-ready low-altitude wind paper should connect the AI method to boundary-layer forecasting difficulty:

- Low-altitude winds are shaped by terrain, surface roughness, stability, diurnal mixing, local circulations, and synoptic forcing.
- Observations are sparse in space and height, while high-resolution NWP can be expensive or biased near complex terrain.
- Rapid inference matters only if it supports nowcasting, UAS operations, wind-energy dispatch, air quality transport, emergency response, or data-assimilation cycling.

Use exact height ranges whenever possible. Replace vague "low altitude" with "10-300 m AGL", "within the lowest 1 km", "tower-level", "near-surface", or "boundary-layer wind profiles".

## Recommended Claim Spine

"We develop a [deep-learning/hybrid] forecasting system for [height/range/region] wind fields that integrates [observations/NWP/reanalysis/terrain] and produces [lead-time] forecasts with [latency]. Evaluation against [baselines] across [sites, terrain, seasons, regimes] shows [skill], while diagnostic analyses reveal [physical behavior and limitations]."

## Essential Evidence

Prioritize these analyses:

- **Lead time**: errors and skill from the shortest to longest forecast horizon.
- **Height**: error profiles or separate results for each level/sensor height.
- **Terrain**: plains, valleys, slopes, ridges, urban/roughness classes, or other local categories.
- **Time**: day/night, season, diurnal transition, synoptic regimes.
- **Events**: ramps, gusts, strong-wind thresholds, low-level jets if relevant.
- **Generalization**: leave-one-station/site/region-out and independent periods.
- **Uncertainty**: prediction intervals, ensemble spread, calibration, or error stratification.
- **Latency**: inference time, hardware, input update frequency, and forecast-cycle fit.

## Baselines

Use the strongest baselines available:

- Persistence for short lead times.
- Climatology or diurnal climatology.
- Linear/ARIMA/Kalman/filtering or simple statistical nowcast.
- LSTM/GRU/TCN/ConvLSTM/U-Net/Transformer/GNN baselines depending on data geometry.
- NWP forecasts, WRF output, HRRR, ERA5/ERA5-Land, or operational model products if available.
- Bias-corrected NWP or MOS-style baseline when claiming postprocessing improvements.

## Physical Diagnostics

Use at least some diagnostics beyond scalar accuracy:

- Wind-speed and direction joint errors.
- Vector wind components (u/v) and speed/direction metrics.
- Vertical shear and profile shape.
- Spatial coherence and gradients.
- Spectral or scale-dependent error.
- Terrain-conditioned residual maps.
- Case studies for frontal passage, valley wind, nocturnal jet, convective outflow, or ramp events.
- Sensitivity to terrain, land-surface, stability, and upstream observations.

## Wording Choices

Use:

- "low-level wind-field forecasting"
- "tower-level wind-speed prediction"
- "boundary-layer wind profile forecasting"
- "rapid neural inference"
- "terrain-aware generalization"
- "lead-time-dependent skill"

Avoid unless fully supported:

- "real-time prediction" without latency and input availability.
- "universal model" without transfer tests.
- "physical mechanism learned by the model" without diagnostic evidence.
- "high-resolution wind field" without spatial resolution and validation density.

## Likely Reviewer Questions

- Why is deep learning needed beyond NWP bias correction or MOS?
- Does the model generalize to stations or terrain not seen during training?
- Are improvements dominated by easy calm-wind cases?
- How does wind direction error behave near low speeds?
- Does the model preserve vertical shear and flow continuity?
- Are extreme/ramp events improved or smoothed out?
- Is inference fast enough relative to data arrival and forecast cycle?
- Can the method be reproduced from public or archived data/code?
