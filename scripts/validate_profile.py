"""Fail closed when the public GitHub profile loses its evidence boundary."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
REVISION = "e18877dddd277fb250e8427af67f33f1f507fc04"

failures: list[str] = []


def require(text: str, message: str) -> None:
    if text not in README:
        failures.append(message)


for phrase in (
    "predictive machine learning",
    "generative AI",
    "tool-using agent systems",
    "production feedback",
    "| 10 |",
    "31,389",
    "588",
    "not model rankings, production prevalence estimates, or deployment",
    "https://vyomagajjar.com/evidence.json",
    "bounded claim, source class, evidence locator",
):
    require(phrase, f"missing required positioning or claim boundary: {phrase}")

for path in (
    "research/EVALS.md",
    "research/FINDINGS.md",
    "templates/agent-scale-decision-contract.md",
    "templates/agent-decision-record.template.json",
    "examples/agent-decision-record.json",
    "agent_economics/decision_record.py",
    "templates/production-feedback-contract.template.json",
    "examples/production-feedback-contract.json",
    "agent_economics/feedback_contract.py",
    "docs/novelty.md",
    "research/HELD_OUT.md",
    "docs/limitations.md",
):
    require(
        f"agent-economics-lab/blob/{REVISION}/{path}",
        f"missing pinned evidence link: {path}",
    )

for receipt in (
    "https://patents.google.com/patent/US11748453B2/en",
    "https://research.ibm.com/publications/navigating-the-complexities-of-generative-ais-ethical-social-and-legal-implications",
    "https://espa.unex.ucla.edu/computer-science/machine-learning-ai/course/building-retrieval-augmented-generation-rag-com-sci",
    "https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/ceg-ai-coe-articles/59/2/ServiceNow_AI_Agents_Well-Architected_Review_v1.pdf",
):
    require(receipt, f"missing independent record: {receipt}")

require(
    f"git -C agent-economics-lab checkout {REVISION}",
    "reproduction command is not pinned to the evidence revision",
)

for stale_phrase in (
    "AI Consulting",
    "GenAI Solutions Expert",
    "AI Agent Evaluation & Systems",
    "economic assurance for AI agents",
    "leading expert",
):
    if stale_phrase.casefold() in README.casefold():
        failures.append(f"stale or promotional positioning remains: {stale_phrase}")

if "\N{EM DASH}" in README:
    failures.append("profile contains an em dash")

if "/blob/main/" in README:
    failures.append("evidence links must be pinned, not linked through blob/main")

links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", README)
for link in links:
    if not (link.startswith("https://") or link.startswith("mailto:")):
        failures.append(f"profile contains a non-HTTPS link: {link}")

if failures:
    raise SystemExit("\n".join(f"FAIL {failure}" for failure in failures))

print("Profile validation passed.")
