---
name: aam-skills
description: Draft, restructure, polish, or reviewer-audit manuscripts for the AGU Journal of Advances in Modeling Earth Systems (JAMES), especially AI, machine learning, deep learning, neural weather model, downscaling, data assimilation, parameterization, and low-altitude wind-field forecasting papers. Use when the user asks for JAMES writing style, JAMES manuscript revision, abstract/key points/plain-language summary, methods/experiments/results/discussion rewriting, AGU open-research compliance, reviewer-style critique, Chinese-to-English academic revision, atmospheric-environment AI papers, or low-altitude wind forecasting manuscripts.
---

# AAM-skills

Use this skill to turn AI-for-atmospheric-modeling work into a JAMES-shaped scientific argument. Prioritize model-system contribution, physical interpretability, rigorous benchmarking, uncertainty/error characterization, reproducibility, and clear Earth-system relevance.

## Quick Routing

1. Identify the job:
   - **Draft/restructure**: user asks to write a section, rebuild the paper story, or plan the manuscript.
   - **Polish/translate**: user provides text and asks for English revision or Nature/JAMES-level language.
   - **Reviewer audit**: user asks whether the manuscript can meet JAMES standards or wants rejection-risk diagnosis.
   - **Submission compliance**: user asks about AGU/JAMES requirements, Key Points, Plain Language Summary, Open Research, data/code availability, or figure/table readiness.
2. Identify section(s): title, abstract, key points, plain-language summary, introduction, data, methods/model, experiments, results, discussion, conclusions, open research, response to reviewers.
3. Identify paper subtype:
   - AI forecast model, neural weather model, downscaling/bias correction, parameterization/emulator, data assimilation/observation error, uncertainty/probabilistic forecast, surface/low-level wind application.
4. Before writing, state one short line with the detected job, section, subtype, and language. Ask only if the missing detail would materially change the output.

## Always Load

Read these references before doing substantive JAMES writing or revision:

- `references/james-core-style.md`
- `references/james-article-architecture.md`
- `references/james-reviewer-checklist.md`

For low-altitude wind-field forecasting, wind-energy, boundary-layer, terrain, tower/UAS/lidar, or surface-wind manuscripts, also read:

- `references/low-altitude-wind-ai.md`

## Conditional References

Load only the relevant files:

- **Abstract, Key Points, Plain Language Summary**: `references/front-matter.md`
- **Introduction, contribution framing, related work**: `references/introduction-framing.md`
- **Data, model, methods, experiments, baselines, ablations**: `references/methods-experiments.md`
- **Results, discussion, limitations, conclusions**: `references/results-discussion.md`
- **AGU/JAMES open research, data/code availability, reproducibility**: `references/open-research-compliance.md`
- **Learning from the supplied local sample PDFs or refreshing the style index**: `references/sample-study-notes.md` and optionally run `scripts/extract_james_patterns.py`

Do not read every reference by default. Keep the working context matched to the user's current section.

## JAMES Revision Workflow

1. Write the paper's one-sentence claim in this form: **For [Earth-system problem], we introduce/evaluate [model or method] that [capability] and show [evidence] under [domain/boundary].**
2. Separate novelty into three layers:
   - Earth-system need: what forecast/modeling limitation matters scientifically or operationally?
   - Modeling advance: what is new about the data, architecture, coupling, physics constraint, uncertainty treatment, or inference workflow?
   - Evidence: what benchmarks, regimes, ablations, and uncertainty analyses prove the claim?
3. Repair the section before polishing sentences. A fluent paragraph with weak baselines, vague data splits, or no physical interpretation is still weak for JAMES.
4. Enforce JAMES front matter: concise title, three Key Points, technical abstract, Plain Language Summary, and Open Research/Data Availability statements.
5. For AI papers, require comparison against meaningful baselines: persistence/climatology, operational NWP or reanalysis-derived forecasts when appropriate, classical ML/statistical models, ablated neural variants, and physically motivated alternatives.
6. For low-altitude wind papers, require terrain/regime/generalization tests when possible: height, lead time, stability, wind-speed bin, diurnal cycle, season, terrain class, station/site leave-out, and extreme/ramp events.
7. End with a reviewer-style audit: list missing evidence, overstated claims, reproducibility gaps, and likely JAMES reviewer objections.

## Writing Standards

- Prefer "modeling system" and "forecasting workflow" framing over generic "we propose a deep learning model."
- Tie every algorithmic detail to an Earth-system reason: boundary-layer structure, terrain forcing, multiscale dynamics, data sparsity, uncertainty growth, computational latency, or operational use.
- Use restrained claims. Do not claim operational readiness without independent validation, latency reporting, robustness tests, and deployment constraints.
- Treat interpretability as evidence, not decoration. Connect attention maps, feature importance, sensitivity tests, spectra, profiles, conservation checks, or case studies to physical behavior.
- Keep Chinese-to-English rewrites precise and direct. Remove inflated phrases, avoid "significant" unless statistically or practically supported, and translate "rapid prediction" as "rapid forecasting/inference" only when speed is quantified.

## Output Format

For writing or revision tasks, return:

1. **Revised text** or **draft text**.
2. **Why it fits JAMES**: 3-6 concise points focused on structure, evidence, and journal expectations.
3. **Needed evidence or checks**: only items that would materially affect acceptance.

For reviewer audits, lead with findings ordered by severity, then give a short revision plan.

For compliance tasks, return a checklist with pass/fail/needs-info labels.

## Sample PDF Index

The user supplied local JAMES papers. This skill stores only structural metadata extracted from those PDFs in:

- `references/james-sample-extraction.md`
- `references/james-relevant-extraction.md`

To refresh the index after adding PDFs:

```bash
python scripts/extract_james_patterns.py "path/to/JAMES PDFs" --json references/james-sample-extraction.json --markdown references/james-sample-extraction.md
```

Use the sample index for patterns such as section order and presence of Key Points/Plain Language Summary/Data Availability. Do not reproduce long source passages from the PDFs.
