# Solution Architecture MCP Toolkit

A portfolio-grade toolkit for Solution Architects who want to use AI agents and MCP-style tools to accelerate architecture work while preserving discipline, governance and documentation quality.

## What it does

The project provides reusable tools and templates for:

- Architecture Decision Records.
- AWS Well-Architected checklists.
- Threat-model prompts and templates.
- Cost and risk review workflows.
- MCP-compatible tool design for architecture assistants.

## Why this matters

AI can help architects move faster, but architecture work still needs explicit decisions, traceability, security review, cost thinking and human accountability. This repository shows how MCP tools can encode architecture practice instead of replacing it with generic chat.

## Run locally

```bash
python -m pip install -e . pytest
sa-toolkit well-architected
sa-toolkit adr --title "Use Amazon EventBridge" --context "Need decoupling" --decision "Adopt EventBridge"
pytest -q
```

## Portfolio positioning

This project connects Solution Architecture, AI tooling, MCP, DevSecOps and documentation practices into a practical open-source toolkit.

## Frontend

```bash
cd frontend
npm ci
npm run lint
npm run build
```

The frontend is a dependency-light static portfolio surface ready for Vercel deployment.

## Operations

See [OPERATIONS.md](OPERATIONS.md) for GitFlow, Vercel secrets and security pipeline details.
