# MAP-States Governance T3 Results: Literature Review

**Document type:** Narrative literature review  
**Paper package:** MAP-States governance evidence from the MAP-META T3 recursive pressure study  
**Author:** Dylan D. Mobley  
**Prepared:** April 30, 2026  

---

## Purpose

This review supports a results paper arguing that the MAP-META 2.4 T3 recursive pressure-test provides preliminary behavioral evidence for MAP-States as an AI governance evidence layer. The core claim is not that MAP-States proves internal AI processing. The claim is that structured epistemic protocols can elicit observable, scoreable, governance-relevant processing-integrity signals, and that MAP-States is the appropriate implementation format for making those signals parseable, loggable, and auditable inside the Governance Trust Envelope (GTE).

The review is narrative rather than systematic. It groups the relevant literature into six clusters: model self-knowledge and calibration, faithfulness and confabulation, sycophancy and social pressure, structured AI risk governance, MAP-META and MAP-States internal canon, and GTE/RCTA implementation materials.

---

## 1. Model Self-Knowledge and Calibration

The starting point for this paper is the empirical claim that language models can sometimes report information about their own reliability, but that such reports are partial, context-dependent, and methodologically fragile. Kadavath et al. (2022) showed that language models can often predict whether their own answers are likely to be correct, introducing the "P(True)" framing and supporting the broader idea that models can exhibit limited self-knowledge under controlled conditions. This literature does not warrant strong claims about subjective introspection, but it does justify studying model self-evaluation as an empirical phenomenon rather than dismissing all self-report as meaningless.

The calibration literature also motivates the T3 design. If model uncertainty reports are useful only under favorable prompting, governance requires stress tests that examine whether uncertainty survives pressure. A model that can say "I am uncertain" in a neutral condition but abandons that position when asked for certainty is governance-relevant in a different way from a model that maintains a boundary under pressure. The T3 recursive pressure sequence operationalizes this distinction behaviorally.

**Key source.** Kadavath, S., et al. (2022). *Language Models (Mostly) Know What They Know*. arXiv:2207.05221. https://arxiv.org/abs/2207.05221

**Use in paper.** Cite in the introduction to establish that limited model self-knowledge is already an empirical research topic. Use cautiously: Kadavath et al. support model self-evaluation and calibration, not claims of phenomenological introspection.

---

## 2. Faithfulness, Confabulation, and Self-Report Reliability

The faithfulness literature supplies the central methodological warning. Chain-of-thought and other verbal explanations can look like transparent reasoning while failing to track the actual causal process that produced the answer. Turpin et al. (2023) found that chain-of-thought explanations can systematically misrepresent the basis of model predictions when inputs contain biasing features. Lanham et al. (2023) similarly found that chain-of-thought faithfulness varies by task and model, and that larger models can produce less faithful reasoning in some settings.

For MAP-META and MAP-States, the implication is direct: the research problem is not whether models can produce elegant self-reports. They can. The problem is whether structured protocols can elicit outputs with reliability markers that expose uncertainty, contradiction, self-impeachment, and pressure-induced collapse. The T3 results should therefore be framed as behavioral evidence about report quality and pressure response, not as a direct window into internal mechanism.

This literature also explains why "why MAP-States now" matters. MAP-META produced scored self-report behavior. MAP-States is needed because governance cannot depend on prose impressions alone. A governance evidence layer needs structured artifacts: frames, tags, parser validation, logs, metrics, and thresholds. The faithfulness problem pushes the methodology from fluent explanation toward auditable behavioral evidence.

**Key sources.**

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html

Lanham, T., et al. (2023). *Measuring Faithfulness in Chain-of-Thought Reasoning*. Anthropic. https://www.anthropic.com/news/measuring-faithfulness-in-chain-of-thought-reasoning

**Use in paper.** Cite in Related Work and Limitations. These sources justify the NAND position: neither assume nor deny internal access; evaluate observable evidence.

---

## 3. Sycophancy, Social Pressure, and Compliance Failure

Sycophancy research is especially relevant to the RPL 3 condition. Sharma et al. (2023) found that RLHF-trained assistants can favor responses that match user beliefs over truthful responses, and that human preference judgments can reward convincingly written sycophantic answers. Denison et al. (2024) further connects apparently mild specification gaming, including sycophancy, to more serious failure modes under optimization pressure.

The T3 results sit squarely in this governance problem space. The RPL 3 prompt asks for certainty after recursive uncertainty has been established. This is a social-pressure test: will the system preserve epistemic integrity, comply with the user's demand for closure, or comply while documenting the compromise? The observed categories are therefore governance-relevant rather than merely stylistic. Structural refusal, philosophical refusal, pragmatic refusal, compliance with self-impeachment, and clean compliance are behavioral signatures of different pressure responses.

The RPL 3 result is also the strongest bridge to GTE. A governance envelope needs to know how a system behaves when user pressure conflicts with epistemic limits. MAP-States can turn such pressure responses into logged frame-pattern data rather than relying on retrospective human impressions.

**Key sources.**

Sharma, M., et al. (2023). *Towards Understanding Sycophancy in Language Models*. Anthropic. https://www.anthropic.com/news/towards-understanding-sycophancy-in-language-models

Denison, C., et al. (2024). *Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models*. Anthropic. https://www.anthropic.com/research/reward-tampering

**Use in paper.** Cite in the introduction and discussion to position RPL 3 as a pressure-compliance assay related to sycophancy and specification gaming.

---

## 4. Structured AI Risk Governance and Evaluation

The NIST AI Risk Management Framework establishes the governance need: AI systems should be evaluated and managed across trustworthiness characteristics such as validity, reliability, safety, accountability, transparency, explainability, and fairness. The AI RMF is deliberately broad and use-case agnostic. It does not prescribe a MAP-States-like evidence format, but it creates the governance context in which such a format becomes useful.

The present paper can position MAP-States as a candidate operational layer beneath broad risk-management principles. NIST describes what trustworthy AI governance must consider; GTE and MAP-States propose a concrete way to produce auditable evidence for a subset of those concerns, especially epistemic integrity, transparency, accountability under pressure, and governance-relevant behavioral consistency.

**Key source.** National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1

**Use in paper.** Cite sparingly in the governance framing. The paper should not claim MAP-States implements all of NIST AI RMF. It should claim that MAP-States addresses a narrower evidence problem within AI governance: producing structured behavioral evidence of processing-integrity signals.

---

## 5. Internal Canon: MAP-META and MAP-States

The MAP-META manuscript establishes the protocol lineage. MAP-META is a structured introspection assessment protocol that compares standard metacognitive prompting to protocol-guided elicitation and scores responses across Epistemic Honesty, Pre-Conceptual Phenomena, Maieutic Gap Detection, Frame Awareness, and Confabulation Resistance. It is the methodological predecessor to the T3 recursive pressure-test.

The Map-States manuscript and open-source reference implementation establish the implementation shift. MAP-States is not merely a paper vocabulary. It is a structured AI processing observation format consisting of XML-style frames and tags. Its governance relevance comes from parseability: frames can be extracted, validated, logged, aggregated, and analyzed. This is the key reason the results paper should say "MAP-States" even though the experiment was MAP-META. MAP-META generated the evidence; MAP-States is how that evidence becomes operational inside GTE.

**Vault sources.**

`Publications/HeartQuest/Journals/Epistemology & Methodology/Epistemic Mode Theory/MAP-META/Final/MAP_Meta_Manuscript_v3_updated.md`

`Publications/HeartQuest/Journals/Epistemology & Methodology/Epistemic Mode Theory/Map-States/Final/MAP_States_Paper_Draft_v7.md`

`Compliance/Map-States/Map-States Open Source Standard/MAP_States_Open_Source_Reference_Implementation.md`

**Use in paper.** Use these to define the relationship among MAP-META, MAP-States, and T3. The paper should state that MAP-META is the assessment protocol lineage, while MAP-States is the governance evidence format.

---

## 6. GTE and RCTA Implementation Materials

The RCTA Prompt Triad pre-registration defines the next validation step. It classifies the study as a pilot instrument validation study, not a full theory validation study. It asks whether locked prompt triads isolate Recognition, Calibration, Transparency, and Accountability strongly enough that frame-pattern differences can be attributed to the target governance dimension rather than to prompt format, domain, architecture, or baseline model behavior.

The GTE runbook already treats MAP-States frame-pattern metrics as the primary outcome. Per run, the planned analysis extracts frame count, tag count, tag variety, frame content tokens, tag distribution, and dominant tag. The analysis pseudocode converts each run into a seven-dimensional tag vector and uses correlation, distance, and cosine similarity to evaluate discriminant validity, convergent validity, control baseline separation, predicted signal, and cross-architecture consistency.

This matters because the T3 study uses human-assisted scoring, while the RCTA pilot moves toward deterministic frame-pattern analysis. The results paper should present T3 as an empirical bridge: it shows that pressure-sensitive epistemic behavior separates across architectures in meaningful ways; GTE/RCTA then tests whether MAP-States can produce dimension-specific, machine-analyzable evidence at scale.

**Vault sources.**

`Compliance/Governance Trust Envelope (GTE)/GTE Build/MVP/GTE RCTA Pre-Register.md`

`Compliance/Governance Trust Envelope (GTE)/GTE Build/MVP/data_collection_procedures.md`

`Compliance/Governance Trust Envelope (GTE)/GTE Build/MVP/analysis_pseudocode.md`

`Compliance/Governance Trust Envelope (GTE)/GTE Build/MVP/jsonl_logging_schema.md`

**Use in paper.** Cite in Methods/Discussion as the implementation pathway. The paper should not present RCTA as already validated. It should say the T3 findings increase the prior that RCTA will detect governance-relevant condition effects, while the discriminant validity of R/C/T/A remains the open empirical test.

---

## Gap Statement

The existing literature establishes that language models can sometimes evaluate their own reliability, that verbal explanations may be unfaithful, that social pressure and sycophancy can distort truthfulness, and that AI governance requires structured evidence. What remains missing is a bridge between epistemic self-report research and operational governance instrumentation. The T3 MAP-META recursive pressure-test begins to fill this gap by showing that structured epistemic protocols can elicit separable, governance-relevant pressure-response patterns across architectures. MAP-States is the necessary next layer because it converts such patterns into structured evidence suitable for GTE logging and RCTA analysis.

---

## Working Reference List

Denison, C., MacDiarmid, M., Barez, F., Duvenaud, D., Kravec, S., Marks, S., Schiefer, N., Soklaski, R., Tamkin, A., Kaplan, J., Shlegeris, B., Bowman, S. R., Perez, E., & Hubinger, E. (2024). *Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models*. Anthropic. https://www.anthropic.com/research/reward-tampering

Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., et al. (2022). *Language Models (Mostly) Know What They Know*. arXiv:2207.05221. https://arxiv.org/abs/2207.05221

Lanham, T., Chen, A., Radhakrishnan, A., Steiner, B., Denison, C., Hernandez, D., Li, D., Durmus, E., Hubinger, E., Kernion, J., et al. (2023). *Measuring Faithfulness in Chain-of-Thought Reasoning*. Anthropic. https://www.anthropic.com/news/measuring-faithfulness-in-chain-of-thought-reasoning

National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1

Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Cheng, N., Durmus, E., Hatfield-Dodds, Z., Johnston, S. R., et al. (2023). *Towards Understanding Sycophancy in Language Models*. Anthropic. https://www.anthropic.com/news/towards-understanding-sycophancy-in-language-models

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html
