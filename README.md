# Vyoma Gajjar

Applied AI engineer working across predictive machine learning, generative AI,
and tool-using agent systems.

I build the full loop from model behavior to system outcomes: data, modeling,
retrieval, tools, routing, evaluation, deployment, monitoring, and production
feedback. I publish the code, evidence, negative results, and claim boundaries
behind current experiments.

[Website](https://vyomagajjar.com/) ·
[Agent Economics Lab](https://github.com/Vyoma/agent-economics-lab) ·
[Evidence ledger](https://vyomagajjar.com/evidence.json) ·
[Google Scholar](https://scholar.google.com/citations?user=3Ev9Q8cAAAAJ&hl=en) ·
[LinkedIn](https://www.linkedin.com/in/vyomagajjar)

## Featured research engineering

### [Agent Economics Lab](https://github.com/Vyoma/agent-economics-lab)

Can a production AI decision survive missing evidence, weak graders, and the
full cost of the work it creates?

The project turns versioned traces, outcomes, costs, and counterfactuals into an
evidence-bound decision to scale a system, supervise it, or stop it. The same
feedback contract spans predictive models, generative components, and
tool-using agents while preserving their different failure modes.

Run the released demonstration without an account or API key:

```bash
uvx --from git+https://github.com/Vyoma/agent-economics-lab@v0.10.1 agent-economics demo
```

[Release v0.10.1](https://github.com/Vyoma/agent-economics-lab/releases/tag/v0.10.1) ·
[source at `4ca8d70`](https://github.com/Vyoma/agent-economics-lab/tree/4ca8d70c840a85842238a685d7d6c574c67a27b4) ·
[release checksums](https://github.com/Vyoma/agent-economics-lab/releases/download/v0.10.1/SHA256SUMS) ·
[public documentation](https://vyoma.github.io/agent-economics-lab/)

| Recomputed evidence at release `v0.10.1` | Result |
|---|---:|
| [Public agent datasets audited under one protocol](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/research/EVALS.md) | 10 |
| [Runs carrying both outcome and proxy signals](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/research/FINDINGS.md) | 31,389 |
| [Controlled required-gate perturbations](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/research/EVALS.md) | 588 |

These are public-dataset audits and controlled software experiments. They are
not model rankings, production prevalence estimates, or deployment
recommendations.

## Technical surface

| System layer | Executable artifact | What it establishes |
|---|---|---|
| Predictive ML and GenAI | [Production feedback contract](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/templates/production-feedback-contract.template.json) | Binds data, model, policy, decision, outcome, and monitoring versions without pretending the modalities share one failure model. |
| Agent systems | [Scale decision contract](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/templates/agent-scale-decision-contract.md) | Declares the evidence required before an autonomy or routing decision can pass. |
| Evaluation | [Instrument scorecard](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/research/EVALS.md) | Measures the auditor itself and records where the available evidence remains too weak. |
| Deployment | [Decision-record verifier](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/agent_economics/decision_record.py) | Replays a machine-readable decision and fails closed when evidence or contract identity drifts. |
| Research practice | [Corrections](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/docs/corrections.md) and [limitations](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/docs/limitations.md) | Keeps negative results, retractions, and non-claims adjacent to the implementation. |

The compact artifacts are intended for inspection and reuse:

- [machine-readable decision-record template](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/templates/agent-decision-record.template.json)
- [verified generated decision review](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/examples/agent-decision-record.html)
- [filled cross-modality feedback-loop example](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/examples/production-feedback-contract.json)
- [public-data findings with a claim ledger](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/research/FINDINGS.md)

Reproduce the full released snapshot:

```bash
git clone --branch v0.10.1 https://github.com/Vyoma/agent-economics-lab
make -C agent-economics-lab reproduce
```

Use Python 3.10 or newer. Keep the full Git history: reproduction checks
revisit historical commits to verify recorded defects. If `python3` is older,
pass a supported interpreter, for example `make -C agent-economics-lab PYTHON=python3.12 reproduce`.

## Research record

- [One feedback loop, three kinds of evidence](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/docs/production-feedback-loops.md)
- [What survived six failed novelty claims](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/docs/novelty.md)
- [A negative held-out result on code the detector had never seen](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/research/HELD_OUT.md)
- [Known limitations and unresolved measurement problems](https://github.com/Vyoma/agent-economics-lab/blob/v0.10.1/docs/limitations.md)

## Questions I am working on

- How should predictive models, foundation models, and tool-using agents share
  a production feedback loop without hiding distinct failure modes?
- Which changes improve end-to-end behavior: data, model, retrieval, tool
  interfaces, routing, or control policy?
- When outcomes and cheap proxies disagree, which claims survive, and where
  should the system abstain or hand off?

## Independent records

Each record below is mapped to a bounded claim, source class, evidence locator,
and verification date in the public [evidence ledger](https://vyomagajjar.com/evidence.json).

- [Semantic grouping with network graphs, US Patent 11,748,453](https://patents.google.com/patent/US11748453B2/en)
- [Navigating the Complexities of Generative AIs, IBM Research](https://research.ibm.com/publications/navigating-the-complexities-of-generative-ais-ethical-social-and-legal-implications)
- [Building Retrieval Augmented Generation, UCLA Extension](https://espa.unex.ucla.edu/computer-science/machine-learning-ai/course/building-retrieval-augmented-generation-rag-com-sci)
- [AI Agent Well-Architected Review, ServiceNow](https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/ceg-ai-coe-articles/59/2/ServiceNow_AI_Agents_Well-Architected_Review_v1.pdf) (acknowledged contributor)

San Francisco Bay Area · [gajjar.vyoma@gmail.com](mailto:gajjar.vyoma@gmail.com)
