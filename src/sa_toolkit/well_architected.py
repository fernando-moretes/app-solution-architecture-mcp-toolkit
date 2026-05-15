PILLARS = ("operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization", "sustainability")

QUESTION_BANK = {
    "security": ["How are identities authenticated and authorized?", "How is data protected in transit and at rest?", "How are secrets managed?"],
    "reliability": ["What are the failure modes?", "How does the system recover?", "Are retries bounded and observable?"],
    "cost-optimization": ["What is the cost per transaction?", "Which resources scale to zero?", "Are expensive paths measured?"],
    "operational-excellence": ["What are the runbooks?", "Which metrics indicate customer impact?"],
    "performance-efficiency": ["What are p95 and p99 latency targets?", "How are model/tool bottlenecks detected?"],
    "sustainability": ["Can smaller models or caches reduce compute?", "What data retention policy reduces waste?"],
}

def checklist(pillars: tuple[str, ...] = PILLARS) -> str:
    lines = ["# Well-Architected Checklist", ""]
    for pillar in pillars:
        lines.append(f"## {pillar.replace('-', ' ').title()}")
        for q in QUESTION_BANK[pillar]:
            lines.append(f"- [ ] {q}")
        lines.append("")
    return "
".join(lines)

def risk_level(open_items: int) -> str:
    if open_items <= 3:
        return "low"
    if open_items <= 8:
        return "medium"
    return "high"
