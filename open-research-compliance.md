# Open Research And Submission Compliance

Use this reference for AGU/JAMES-facing compliance checks. Always verify current journal instructions before final submission because publisher requirements can change.

## Front-Matter Checklist

Check for:

- Title.
- Three Key Points.
- Abstract.
- Plain Language Summary.
- Data Availability Statement or Open Research section.
- Acknowledgments and funding.
- References.

## Data Availability

A JAMES manuscript should make data traceable:

- Public repository and persistent identifier where possible.
- Exact data versions, access dates if relevant, and license or restrictions.
- Clear separation between raw observations, processed data, model outputs, trained weights, and scripts.
- If data are restricted, state the restriction and provide the strongest available access route.

Avoid vague statements such as "data are available upon request" unless no stronger option is possible and the reason is explicit.

## Code And Software

For AI/modeling manuscripts, report:

- Code repository or archive.
- Release version or commit hash.
- License.
- Environment or dependency file.
- Training/inference scripts.
- Evaluation scripts or notebooks.
- Trained weights if needed for reproduction and allowed.
- Configuration files for experiments.

If a model uses large external data or operational systems, archive the preprocessing and configuration needed to recreate the workflow.

## Figures And Tables

Check that:

- Figures support claims directly.
- Axes include units.
- Color scales are interpretable and comparable across panels.
- Maps include region, projection, and meaningful labels.
- Error bars or confidence intervals appear when differences are small.
- Tables define metrics, baselines, lead times, heights, and regimes.

## Ethical And Reporting Boundaries

Do not overstate:

- Operational readiness.
- Generalization beyond the test domain.
- Physical causality from correlation or feature importance.
- Real-time capability without latency and input availability.
- Climate relevance from short-period weather tests unless explicitly justified.

## Compliance Output

When asked for a compliance check, use:

- `Pass`: present and adequate.
- `Needs revision`: present but incomplete or weak.
- `Missing`: absent.
- `Needs journal verification`: likely requirement, but final current instruction should be checked.
