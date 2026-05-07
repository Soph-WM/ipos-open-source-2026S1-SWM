# Contributing Guidelines

Thank you for your interest in contributing to this project.
This repository is designed as both:

- an educational resource
- and an evolving engineering project exploring FastAPI, MCP servers, APIs, streaming, and AI integration patterns.
  Contributions are welcome provided they align with the goals and architecture of the project.

---

# Project Philosophy

This project follows a progressive engineering model:

```text
CLI Application
    ↓
Refactored Logic
    ↓
REST API
    ↓
MCP Server
    ↓
Streaming + AI Integration
```

The goal is to help developers understand:

- software evolution
- API architecture
- MCP concepts
- event-driven systems
- AI tooling integration
  Please avoid introducing unnecessary complexity or large architectural changes without discussion first.

---

# Before Contributing

Before opening a Pull Request (PR):

1. Read the README, SPEC and all documentation
2. Check existing Issues and Discussions
3. Open a discussion for large changes
4. Keep contributions focused and incremental

---

# Recommended Contribution Areas

Contributions are especially welcome in the following areas:

## Documentation

- Tutorials
- Diagrams
- Architecture explanations
- MCP examples
- Setup improvements

## Testing

- pytest improvements
- MCP lifecycle tests
- Error handling tests
- Streaming tests

## FastAPI Improvements

- Route organisation
- Dependency injection
- Validation improvements
- Async handling

## MCP Features

- Tools
- Resources
- Prompts
- Streaming/event workflows
- Inspector compatibility

## Developer Experience

- Docker support
- CI/CD improvements
- Better setup instructions
- Debugging workflows

---

# Coding Guidelines

## Python Style

- Follow PEP8 where practical
- Prefer readable code over clever code
- Keep functions focused and small
- Add comments where logic is non-obvious

## Architecture

- Separate business logic from transport layers
- Avoid tightly coupling API routes to logic
- Keep MCP concerns isolated where possible
- Prefer progressive refactoring over rewrites

## Naming

Use the Organisation **code-style-guide.md** Use clear descriptive naming.
Good:

```python
get_task_by_id()
create_mcp_tool_response()
```

Avoid:

```python
doThing()
handleStuff()
```

---

# Branch Workflow

Recommended workflow:

```text
main
 └── feature/your-feature-name
```

Example:

```text
feature/add-streaming-events
feature/mcp-resource-support
feature/pytest-lifecycle-tests
```

---

# Pull Request Guidelines

Please ensure PRs:

- are focused on a single improvement
- include a clear description
- explain WHY the change is needed
- avoid unrelated formatting changes
- include tests where appropriate
  Large PRs are harder to review and may be delayed.

---

# Commit Message Suggestions

Examples:

```text
Add MCP tools/list lifecycle test
Refactor task service into separate module
Improve FastAPI validation handling
Add streaming event example
Fix JSON-RPC error handling
```

---

# Discussions

Use Discussions for:

- architecture questions
- design ideas
- MCP experimentation
- learning questions
- AI integration concepts
  Use Issues for:
- bugs
- reproducible problems
- feature requests
- documentation errors

---

# Educational Focus

This repository intentionally prioritises:

- clarity
- maintainability
- learning value
- architectural understanding
  Some implementations may be intentionally simplified to support teaching and experimentation.

---

# Code of Conduct

Please keep all interactions:

- respectful
- constructive
- professional
- technically focused
  Harassment, insulting behaviour, or disruptive conduct will not be tolerated.

---

# Final Notes

The purpose of this project is not only to build software,
but to explore how modern AI-capable systems are architected.
Thank you for contributing and helping improve the project.
