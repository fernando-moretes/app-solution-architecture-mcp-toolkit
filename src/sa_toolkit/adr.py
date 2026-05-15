from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class ADR:
    title: str
    context: str
    decision: str
    consequences: list[str]
    status: str = "Proposed"

    def to_markdown(self) -> str:
        consequences = "
".join(f"- {item}" for item in self.consequences)
        slug_title = self.title.strip()
        return f"""# ADR: {slug_title}

Date: {date.today().isoformat()}
Status: {self.status}

## Context

{self.context}

## Decision

{self.decision}

## Consequences

{consequences}
"""

def build_adr(title: str, context: str, decision: str, consequences: list[str] | None = None) -> ADR:
    return ADR(title=title, context=context, decision=decision, consequences=consequences or ["Decision must be reviewed by architecture stakeholders."])
