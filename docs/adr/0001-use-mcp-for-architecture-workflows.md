# ADR 0001: Use MCP for Architecture Workflows

## Status

Accepted

## Context

Architecture work requires repeatable tools for ADRs, risks, cost and security. Generic prompts are hard to govern.

## Decision

Expose architecture workflows as MCP-compatible tools with typed inputs and deterministic templates.

## Consequences

- Positive: more repeatable architecture outputs.
- Positive: easier integration with agentic assistants.
- Negative: templates need maintenance as standards evolve.
