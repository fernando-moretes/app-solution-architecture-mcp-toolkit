from sa_toolkit.adr import build_adr

adr = build_adr(
    title="Use Amazon Bedrock Guardrails",
    context="Agentic AI workloads need responsible AI controls.",
    decision="Apply guardrails at the model interaction boundary.",
    consequences=["Improves governance.", "Requires policy lifecycle management."],
)
print(adr.to_markdown())
