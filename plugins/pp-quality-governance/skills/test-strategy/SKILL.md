---
name: test-strategy
description: Define test strategy: unit tests for plug-ins, Test Engine / EasyRepro UI tests, flow smoke tests and UAT. Use when planning quality assurance.
---

# Test strategy

| Layer | Tool |
|---|---|
| Plug-ins | Unit tests with FakeXrmEasy / XrmMockup |
| Canvas apps | Power Apps Test Engine (`pac test run`) |
| Model-driven UI | EasyRepro / Playwright |
| Flows | Trigger with test data; verify run history; smoke test after deploy |
| Agents | Copilot Studio evaluation sets |
| Security | One test user per role |
| Performance | Representative data volume in TEST |

Run unit + smoke tests in the pipeline; manual UAT only for acceptance.
