# Vyoma Gajjar

Applied AI engineer working across predictive machine learning, generative AI,
and tool-using agent systems.

I build the full loop from model behavior to system outcomes: data, modeling,
retrieval, tools, routing, evaluation, deployment, monitoring, and production
feedback. I publish the code, evidence, and negative results behind current
experiments.

[Website](https://vyomagajjar.com/) ·
[Agent Economics Lab](https://github.com/Vyoma/agent-economics-lab) ·
[LinkedIn](https://www.linkedin.com/in/vyomagajjar)

## Featured research engineering

### [Agent Economics Lab](https://github.com/Vyoma/agent-economics-lab)

Can an agent decision survive missing evidence, weak graders, and the cost of
the work it creates?

This standard-library-only Python project audits whether the evidence around an
agent supports a decision to expand it, supervise it, or switch it off. It
combines trace-to-outcome evaluation, full-cost accounting, label-quality
audits, and reproducible decision and feedback records.

| Evidence at revision [`e18877d`](https://github.com/Vyoma/agent-economics-lab/tree/e18877dddd277fb250e8427af67f33f1f507fc04) | Result |
|---|---:|
| [Public agent datasets audited under one protocol](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/research/EVALS.md) | 10 |
| [Runs carrying both outcome and proxy signals](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/research/FINDINGS.md) | 31,389 |
| [Controlled required-gate perturbations](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/research/EVALS.md) | 588 |

These are public-dataset audits and controlled software experiments. They are
not model rankings, production prevalence estimates, or deployment
recommendations.

## Reusable system artifacts

- [One-page scale decision contract](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/templates/agent-scale-decision-contract.md)
- [Machine-readable decision record template](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/templates/agent-decision-record.template.json)
- [Filled decision record](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/examples/agent-decision-record.json)
- [Verifier that replays the decision](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/agent_economics/decision_record.py)
- [Cross-modality production feedback contract](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/templates/production-feedback-contract.template.json)
- [Filled synthetic feedback-loop example](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/examples/production-feedback-contract.json)
- [Feedback-contract validator and canonical digest](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/agent_economics/feedback_contract.py)
- [Instrument scorecard with explicit non-claims](https://github.com/Vyoma/agent-economics-lab/blob/e18877dddd277fb250e8427af67f33f1f507fc04/research/EVALS.md)

Reproduce the pinned snapshot:

```bash
git clone https://github.com/Vyoma/agent-economics-lab.git
git -C agent-economics-lab checkout e18877dddd277fb250e8427af67f33f1f507fc04
make -C agent-economics-lab reproduce
```

## Questions I am working on

- How should predictive models, foundation models, and tool-using agents share
  a production feedback loop without hiding distinct failure modes?
- Which changes improve end-to-end behavior: data, model, retrieval, tool
  interfaces, routing, or control policy?
- When outcomes and cheap proxies disagree, which claims survive, and where
  should the system abstain or hand off?

## Independent records

- [Semantic grouping with network graphs, US Patent 11,748,453](https://patents.google.com/patent/US11748453B2/en)
- [Navigating the Complexities of Generative AIs, IBM Research](https://research.ibm.com/publications/navigating-the-complexities-of-generative-ais-ethical-social-and-legal-implications)
- [Building Retrieval Augmented Generation, UCLA Extension](https://espa.unex.ucla.edu/computer-science/machine-learning-ai/course/building-retrieval-augmented-generation-rag-com-sci)
- [AI Agent Well-Architected Review, ServiceNow](https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/ceg-ai-coe-articles/59/2/ServiceNow_AI_Agents_Well-Architected_Review_v1.pdf) (acknowledged contributor)

San Francisco Bay Area · [gajjar.vyoma@gmail.com](mailto:gajjar.vyoma@gmail.com)
