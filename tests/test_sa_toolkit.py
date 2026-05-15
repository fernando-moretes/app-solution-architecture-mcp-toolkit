from sa_toolkit.adr import build_adr
from sa_toolkit.well_architected import checklist, risk_level

def test_adr_markdown_contains_decision_sections():
    md = build_adr("Use EventBridge", "Need decoupling", "Adopt EventBridge").to_markdown()
    assert "# ADR: Use EventBridge" in md
    assert "## Context" in md
    assert "Adopt EventBridge" in md

def test_well_architected_checklist_contains_all_pillars():
    md = checklist()
    assert "Security" in md
    assert "Reliability" in md
    assert "Cost Optimization" in md

def test_risk_level_classification():
    assert risk_level(2) == "low"
    assert risk_level(6) == "medium"
    assert risk_level(12) == "high"
