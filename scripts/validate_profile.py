"""Fail closed when the public GitHub profile loses its evidence boundary."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
RELEASE = "v0.10.1"
SOURCE_COMMIT = "4ca8d70c840a85842238a685d7d6c574c67a27b4"

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
    "verified generated decision review",
    "Run the released demonstration without an account or API key",
    "release checksums",
    "Predictive ML and GenAI",
    "Agent systems",
    "Research practice",
):
    require(phrase, f"missing required positioning or claim boundary: {phrase}")

for path in (
    "research/EVALS.md",
    "research/FINDINGS.md",
    "templates/agent-scale-decision-contract.md",
    "templates/agent-decision-record.template.json",
    "examples/agent-decision-record.html",
    "agent_economics/decision_record.py",
    "templates/production-feedback-contract.template.json",
    "examples/production-feedback-contract.json",
    "docs/corrections.md",
    "docs/novelty.md",
    "research/HELD_OUT.md",
    "docs/limitations.md",
    "docs/production-feedback-loops.md",
):
    require(
        f"agent-economics-lab/blob/{RELEASE}/{path}",
        f"missing pinned evidence link: {path}",
    )

for release_receipt in (
    f"agent-economics-lab@{RELEASE} agent-economics demo",
    f"agent-economics-lab/releases/tag/{RELEASE}",
    f"agent-economics-lab/releases/download/{RELEASE}/SHA256SUMS",
    f"agent-economics-lab/tree/{SOURCE_COMMIT}",
):
    require(release_receipt, f"missing release receipt: {release_receipt}")

for receipt in (
    "https://patents.google.com/patent/US11748453B2/en",
    "https://research.ibm.com/publications/navigating-the-complexities-of-generative-ais-ethical-social-and-legal-implications",
    "https://espa.unex.ucla.edu/computer-science/machine-learning-ai/course/building-retrieval-augmented-generation-rag-com-sci",
    "https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/ceg-ai-coe-articles/59/2/ServiceNow_AI_Agents_Well-Architected_Review_v1.pdf",
):
    require(receipt, f"missing independent record: {receipt}")

require(
    f"git clone --branch {RELEASE} "
    "https://github.com/Vyoma/agent-economics-lab",
    "reproduction command is not pinned to the released evidence",
)

if re.search(r"--(?:depth|shallow-since|shallow-exclude)\b", README):
    failures.append("full reproduction requires Git history; do not advertise a shallow clone")

if "d56e2ffa1dff77dc2985fcc68ec114da0009041c" in README:
    failures.append("profile still points at the superseded pre-release snapshot")

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
