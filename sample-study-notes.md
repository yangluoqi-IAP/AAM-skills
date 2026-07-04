# Sample Study Notes

Use this reference when learning from the local JAMES PDF samples supplied by the user.

## What The Sample Index Shows

The local sample extraction files indicate recurring JAMES conventions:

- Articles commonly include Abstract, Key Points, Plain Language Summary, Introduction, Data/Methods/Model sections, Results or Results and Discussion, Conclusions or Discussion and Conclusions, Data Availability Statement, References, and Acknowledgments.
- AI and machine-learning papers are framed through modeling needs: parameterization, weather prediction, uncertainty, downscaling, observation error, surface wind correction, and hybrid physics-ML systems.
- Strong papers report both method construction and evaluation design, rather than treating neural architecture as sufficient novelty.
- Plain Language Summaries translate the modeling problem into societal, operational, or scientific stakes.
- Key Points are findings/contributions, not section summaries.

## Relevant Local Sample Themes

The user's closest JAMES examples include:

- Wind-turbine LES/RANS and wind-farm parameterization.
- Machine-learning prediction of spatiotemporal uncertainty in wind reanalyses.
- Hybrid physics-ML atmospheric modeling.
- Offline surface multilayer model for surface wind-speed forecast correction.
- Calibrated ensembles of neural weather model forecasts.
- UAS observation error variance for data assimilation.
- Diffusion-based downscaling and bias correction of subseasonal wind forecasts.

Use these as style and architecture guides, not as text to copy.

## How To Refresh

Run:

```bash
python scripts/extract_james_patterns.py "path/to/JAMES PDFs" --json references/james-sample-extraction.json --markdown references/james-sample-extraction.md
```

For wind/AI-relevant files:

```bash
python scripts/extract_james_patterns.py "path/to/JAMES PDFs" --json references/james-relevant-extraction.json --markdown references/james-relevant-extraction.md --match "Wind|wind|Machine|Neural|Downscaling|Surface|UAS|Hybrid|turbine"
```

Keep extracted files structural. Do not store long abstract excerpts or full article text inside the skill.
