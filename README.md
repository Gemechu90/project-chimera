# Project Chimera

**Project Chimera** is a modular, agent-based system designed to plan, execute, and evaluate complex tasks through coordinated AI agents and reusable skills. It follows a clean, research-driven architecture that emphasizes extensibility, orchestration, and evaluation.

---

## Overview

Project Chimera implements a multi-agent workflow where tasks are decomposed, executed, and judged in a structured pipeline. The system is built to support experimentation, research, and production-oriented development by separating concerns across agents, skills, orchestration logic, and external services.

At its core, Chimera enables:

* Intelligent task planning
* Skill-based task execution
* Automated evaluation and feedback
* Scalable orchestration and state management

---

## Key Features

* Planner–Worker–Judge agent architecture
* Pluggable and extensible skills system
* Centralized task queue and state manager
* Research-backed design decisions
* External data integration via MCP servers
* Automated testing and CI/CD
* Dockerized deployment support

---

## Project Architecture

Project Chimera follows a layered, agent-centric architecture designed for clarity, extensibility, and evaluation.

### High-Level Architecture Diagram

```text
+---------------------------------------------------+
|                   User / Input                    |
+--------------------------+------------------------+
                           |
                           v
+---------------------------------------------------+
|                  Orchestrator                     |
|  +------------------+   +----------------------+  |
|  |   Task Queue     |-->|   State Manager      |  |
|  +------------------+   +----------------------+  |
+-------------+---------------------+---------------+
              |                     |
              v                     v
+----------------------+   +-----------------------+
|     Planner Agent    |   |     Judge Agent       |
|  (Task Decomposition)|   | (Evaluation & Review) |
+-----------+----------+   +-----------+-----------+
            |                          ^
            v                          |
+----------------------+               |
|     Worker Agent     |---------------+
| (Skill Execution)    |
+-----------+----------+
            |
            v
+---------------------------------------------------+
|                    Skills                         |
|  +-------------+  +----------------+  +---------+|
|  | Trend       |  | Content        |  | Engage  ||
|  | Fetcher     |  | Generator      |  | Manager ||
|  +-------------+  +----------------+  +---------+|
+--------------------------+------------------------+
                           |
                           v
+---------------------------------------------------+
|                MCP Servers / External APIs        |
|              (e.g., News Server)                  |
+---------------------------------------------------+
```

This diagram illustrates how tasks flow from the orchestrator through agents, skills, and external services.

---

## Folder Structure

```text
project-chimera/
├── specs/          # Functional, technical, and architectural specifications
├── research/       # Architecture and tooling research documents
├── skills/         # Modular skill implementations
├── agents/         # Planner, Worker, and Judge agents
├── orchestrator/   # Task queue and state management
├── mcp_servers/    # External service integrations
├── tests/          # Unit and integration tests
├── docker/         # Docker configuration
└── .github/        # CI/CD workflows
```

---

## Specifications

The `specs/` directory defines the formal system requirements:

* `_meta.md` – Specification metadata and scope
* `functional.md` – Functional requirements and system behavior
* `technical.md` – Technical constraints, assumptions, and decisions
* `architecture.md` – System architecture and component interaction

These documents serve as the authoritative reference for system design.

---

## Research & Design Rationale

The `research/` folder captures exploratory and justification documents that inform system design:

* `architecture_strategy.md` – Architectural patterns and trade-offs
* `tooling_strategy.md` – Tool and framework selection rationale

This separation ensures clarity between requirements and exploratory research.

---

## Skills System

Skills are self-contained modules that implement specific capabilities. Each skill follows a consistent interface, allowing agents to discover and invoke them dynamically.

### Existing Skills

* **Trend Fetcher** – Retrieves and analyzes trending information
* **Content Generator** – Produces structured or unstructured content
* **Engagement Manager** – Optimizes interaction and engagement logic

### Adding a New Skill

1. Create a new directory under `skills/`
2. Implement the skill logic in `skill.py`
3. Expose the skill via a consistent interface
4. Add corresponding tests

---

## Agents

Chimera uses a three-agent pattern:

* **Planner Agent** (`agents/planner/`)
  Decomposes high-level objectives into executable tasks.

* **Worker Agent** (`agents/worker/`)
  Executes tasks using available skills.

* **Judge Agent** (`agents/judge/`)
  Evaluates outputs, validates results, and provides feedback.

This separation enables robust reasoning and evaluation loops.

---

## Orchestration Flow

### Task Lifecycle Diagram

```text
[ Task Created ]
        |
        v
[ Task Queued ]
        |
        v
[ Planner Agent ]
        |
        v
[ Task Breakdown ]
        |
        v
[ Worker Agent ]
        |
        v
[ Skill Execution ]
        |
        v
[ Result Generated ]
        |
        v
[ Judge Agent ]
        |
        v
[ Evaluation & Feedback ]
        |
        v
[ State Updated ]
        |
        v
[ Task Completed ]
```

### Orchestrator Responsibilities

The orchestrator ensures reliable execution by:

* Scheduling tasks through the queue
* Tracking execution state
* Coordinating agent interactions
* Handling failures and retries

Core components:

* `task_queue.py` – Manages task scheduling
* `state_manager.py` – Tracks task and system state

---

## MCP Servers

MCP servers provide access to external data sources and services.

* `news_server.py` – Example server for retrieving news or external content

These servers decouple external dependencies from core system logic.

---

## Installation & Setup

### Prerequisites

* Python 3.10+
* Docker (optional)

### Setup Steps

1. Clone the repository
2. Create a `.env` file based on `.env.example`
3. Install dependencies using `pyproject.toml`
4. Verify setup by running tests

---

## Running the Project

### Local Execution

Use the Makefile or direct Python execution to run agents and orchestrator components.

### Docker

A Dockerfile is provided in the `docker/` directory for containerized deployment.

---

## Testing

The `tests/` directory contains:

* Unit tests for individual skills
* Interface compliance tests
* End-to-end pipeline tests

Run tests using your preferred Python test runner.

---

## CI/CD

Project Chimera uses GitHub Actions for continuous integration.

The workflow:

* Runs tests on each push and pull request
* Ensures code quality and stability

Configuration is located in `.github/workflows/main.yml`.

---

## Configuration

Configuration is managed via:

* Environment variables (`.env`)
* Project configuration files (`pyproject.toml`)

Sensitive values should never be committed to the repository.

---

## Development Guidelines

* Follow modular and readable code practices
* Keep skills atomic and reusable
* Write tests for new functionality
* Document design decisions clearly

---

## Roadmap

Planned improvements may include:

* Additional skills
* Enhanced evaluation strategies
* Distributed orchestration
* Visualization and monitoring tools

---

## Contributing

Contributions are welcome.

Please:

* Fork the repository
* Create a feature branch
* Submit a pull request with clear documentation

---

## License

This project is released under an open-source license. See the LICENSE file for details.
