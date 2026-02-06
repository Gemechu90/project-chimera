# Tooling Strategy – Project Chimera

## 1. Philosophy

Project Chimera follows a strict tooling philosophy:

> Tools must reduce ambiguity, not increase velocity at the cost of correctness.

All tools are selected to support:
- Spec fidelity
- Traceability
- Reproducibility
- AI governance

---

## 2. Development Environment

### Operating System
- Primary: Windows (Developer machine)
- CI: Windows-based GitHub Actions runner

All tooling choices are OS-agnostic.

---

## 3. Python Tooling

### Language
- Python 3.11

### Package Management
- pip (baseline compatibility)
- pyproject.toml for dependency declaration

This ensures:
- Simple onboarding
- CI compatibility
- Toolchain transparency

---

## 4. MCP Tooling (Developer-Facing)

MCP tools are used during development to:
- Observe agent reasoning
- Track execution traces
- Record decision telemetry

Examples:
- MCP Sense (Tenx)
- Filesystem MCP
- Git MCP (optional)

These tools do **not** ship with runtime agents.

---

## 5. Runtime Agent Tools vs Skills

### Skills (Internal)
- Live in `skills/`
- Reusable
- Pure Python
- Deterministic input/output
- Fully testable

Examples:
- trend_fetcher
- content_generator
- engagement_manager

### MCP Servers (External)
- Live in `mcp_servers/`
- Wrap APIs or data sources
- Stateless
- Replaceable without changing agent logic

This separation is critical for:
- Maintainability
- Security
- API volatility resistance

---

## 6. Testing Strategy

Testing follows **Test-Driven Development (TDD)**:

- Tests define agent expectations
- Skills must satisfy test contracts
- Agents are validated end-to-end

Test layers:
- Unit tests for skills
- Integration tests for agent flow
- CI-enforced execution

---

## 7. CI/CD Tooling

GitHub Actions is used for:
- Automated testing
- OS validation (Windows)
- Enforcement of engineering discipline

No code is trusted unless it passes CI.

---

## 8. AI Governance

AI behavior is governed via:
- `.cursor/rules`
- Specs as source of truth
- Judge agent enforcement

This prevents:
- Hallucinated code
- Unsafe autonomy
- Spec drift

---

## 9. Summary

The tooling strategy ensures that:
- Humans stay in control
- AI agents remain predictable
- The system scales safely

Tooling is treated as **infrastructure for trust**, not convenience.
