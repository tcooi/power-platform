---
name: flow-error-handling-pattern
description: Standard try/catch/finally scope pattern, retries and alerting for Power Automate flows. Use for any production flow.
---

# Flow error handling

Structure: `Try` scope -> `Catch` scope (Configure run after: has failed, timed out) -> `Finally` scope (run after all).
- In Catch use `result('Try')` filtered for failed actions; log to a Dataverse error table with run URL (`workflow()` + `run.name`) and notify a channel.
- Set retry policy on flaky connectors (exponential), timeouts on long waits, and concurrency control deliberately.
- Terminate with `Failed` in Catch so the run shows as failed.
- Avoid infinite loops from triggers updating the same row: filter columns and add a guard column.
