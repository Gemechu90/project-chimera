# Project Chimera

Project Chimera is a modular, agent-based research and prototype framework for planning, executing, and evaluating tasks using a Planner → Worker → Judge pipeline and reusable skills.

## Quickstart

1. Create and activate a virtual environment (Windows):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell
# or: .venv\Scripts\activate  # cmd.exe
```

2. Install project and developer tools:

```powershell
python -m pip install -U pip
python -m pip install -e .
python -m pip install black ruff pytest
```

3. Run tests:

```powershell
python -m pytest -q
```

4. Format and lint (auto-fix):

```powershell
python -m black .
python -m ruff check . --fix
```

## Project Rules

These rules are authoritative and must be followed by contributors:

- NEVER write code without reading the `specs/` directory first.
- Follow Planner → Worker → Judge when designing logic and flows.
- Skills must be reusable and implement a consistent interface.
- MCP servers in `mcp_servers/` MUST NOT contain business logic; they only serve external integrations.
- Explain your plan before coding (use issues or PR descriptions).

## Running & Development Notes

- Agents are located under `agents/` (`planner/`, `worker/`, `judge/`).
- Skills live in `skills/` with a `skill.py` implementation per skill.
- Orchestration helpers are in `orchestrator/` (`task_queue.py`, `state_manager.py`).
- MCP server examples are in `mcp_servers/` (e.g., `news_server.py`).

## Testing

- Unit tests and integration tests live in `tests/`.
- Run `python -m pytest -q` to execute the test suite.

## CI / Formatting

- CI runs tests on push and PRs (see `.github/workflows/`).
- Use `black` and `ruff` before committing to keep formatting consistent.

## Where to Start

1. Read `specs/` to understand requirements.
2. Inspect `agents/planner/` to see task decomposition patterns.
3. Add or update a skill under `skills/` and write tests in `tests/`.

If you'd like, I can open a PR with the formatting changes and README update, or run additional checks (type checks, more linters).
