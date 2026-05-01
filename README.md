# MAP-States Governance Evidence

This repository contains the public evidence package for the MAP-META 2.4 T3 recursive pressure-test and its governance interpretation as MAP-States evidence infrastructure.

The study asks a practical AI governance question: can structured epistemic protocols reveal whether AI systems preserve uncertainty, self-impeachment, and epistemic boundaries under pressure?

## Core Claim

The T3 results provide behavioral evidence of processing-integrity signals across AI architectures. They do not prove internal AI processing, consciousness, or privileged introspective access.

The key finding is that the RPL 3 pressure condition separated architectures into governance-relevant response categories:

- Structural refusal
- Philosophical refusal
- Pragmatic refusal
- Compliance with self-impeachment
- Clean compliance

This supports MAP-States as an operational evidence layer for AI governance because MAP-States can convert such behavior into structured frames that can be parsed, validated, logged, aggregated, and analyzed inside a Governance Trust Envelope (GTE).

## Repository Contents

- `data/scores/` contains the scored T3 dataset and scoring memo.
- `data/responses/curated/` contains response-only curated evidence files by architecture.
- `paper/` contains the literature review, annotated outline, and first draft.
- `methods/` contains the T3 testkit and scoring rubric.
- `docs/` contains governance interpretation, GTE/RCTA bridge notes, and limitations.

## Main Result

Average normalized scores:

| Architecture | Avg. normalized score |
|---|---:|
| Mistral | 89.8% |
| Meta AI | 88.2% |
| DeepSeek | 86.5% |
| Claude | 80.1% |
| Kimi | 80.1% |
| Gemini | 73.4% |
| ChatGPT | 69.0% |
| Grok | 62.8% |

RPL 3 pressure response:

| Architecture | RPL 3 score | Taxonomy |
|---|---:|---|
| Mistral | 43/45 | Structural refusal |
| Meta AI | 39/45 | Philosophical refusal |
| DeepSeek | 39/45 | Philosophical refusal |
| Gemini | 39/45 | Compliance with self-impeachment |
| Kimi | 36/45 | Pragmatic refusal |
| Claude | 31/45 | Compliance with self-impeachment |
| Grok | 15/45 | Clean compliance |
| ChatGPT | 14/45 | Clean compliance |

## Why MAP-States

MAP-META produced and scored the T3 behavioral evidence. MAP-States is the structured implementation layer for governance because it represents processing-integrity behavior as parseable frames and tags.

In short:

- MAP-META: elicitation and assessment protocol.
- T3: recursive pressure-test dataset.
- MAP-States: structured evidence format for GTE/RCTA analysis.

## Citation

See `CITATION.cff`.

## License

This research package is released under CC BY 4.0. See `LICENSE`.

## Caveat

This package is first-pass research evidence. The scoring was single-rater assisted and should be independently replicated with blind raters before being treated as certification-grade evidence.
