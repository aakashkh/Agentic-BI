# MCP vs Raw Copy-Paste Prompting

This workshop uses MCP and Fabric skills because Power BI development has moved beyond manual chat snippets. A normal chat window can still explain DAX, but it does not have a reliable, live, schema-aware contract with the model or report files.

---

## The Old Pattern: Raw Prompting

Raw prompting usually looks like this:

1. The developer copies table names, column names, and sample DAX into chat.
2. The model generates a markdown code block.
3. The developer copies the answer into Power BI Desktop.
4. Power BI Desktop throws syntax, binding, or context errors.
5. The developer copies the error back into chat.
6. The cycle repeats until the measure or visual works.

That loop breaks down quickly because Power BI projects are not just text snippets. They contain a model graph, relationships, table metadata, partitions, formatting, report pages, visuals, filters, themes, and schema rules.

---

## 1. State and Context Awareness

Raw prompting forces the developer to paste partial context. That usually means:

- Incomplete table lists.
- Missing relationship direction and cardinality.
- Outdated measure definitions.
- Pasted JSON fragments with no surrounding folder structure.
- Token limits when reports grow beyond a small demo.
- Hidden Desktop state that the model never sees.

MCP gives the agent an abstract API map over the semantic model. Instead of guessing from pasted snippets, the agent can ask the local server for tables, columns, measures, relationships, descriptions, and DAX validation results.

With PBIP and PBIR, the report source files also become readable by the agent. The `powerbi-report-authoring` skill then gives the agent the rules for changing pages, visuals, bindings, themes, and validation artifacts.

The result is less guessing and more grounded authoring.

---

## 2. Deterministic Tool Execution

Raw prompting produces instructions for a human to execute. The model might say:

```DAX
Sales PY =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR('DimDate'[Date])
)
```

That DAX can be useful, but the developer still has to:

- Create the measure in the right table.
- Choose a display folder.
- Apply formatting.
- Add descriptions.
- Check table and column names.
- Repair syntax or model-binding errors.
- Create visuals manually.

With MCP, the agent can execute deterministic operations:

- Add a measure into `SalesMetrics`.
- Set the format string.
- Add a business description.
- Validate the DAX expression.
- Create or adjust relationships.
- Rename objects consistently.
- Write updated TMDL into the PBIP codebase.

With the report authoring skill, the agent can then edit PBIR files directly:

- Create a page folder.
- Add `page.json`.
- Add visual folders.
- Write `visual.json` with correct role bindings.
- Apply layout coordinates and formatting.
- Validate against official PBIR schemas.

The output is no longer only advice. It is a concrete file and model change.

---

## 3. Real-Time Validation Loops

Raw prompting has weak validation. The model cannot know whether the copied result loaded successfully unless the developer reports back.

The MCP and PBIR workflow supports a real validation loop:

1. The agent reads the model through MCP.
2. The agent performs a semantic model change.
3. The agent validates DAX or runs a small read-only query.
4. The agent edits PBIR files with the report authoring skill.
5. The agent validates PBIR JSON schema compliance.
6. Power BI Desktop reloads the project or the Desktop Bridge applies changes.
7. The agent checks status, screenshots, or errors and adjusts before the learner presents the result.

This matters because many report failures are structural rather than linguistic. A visual can have valid JSON but invalid field bindings. A DAX measure can parse but return blank because a relationship is inactive. A date calculation can work but sort incorrectly because the date table lacks a proper marked date column.

The agentic workflow gives the agent a way to observe and repair those failures before the report reaches the screen.

---

## Summary

| Area | Raw prompting | MCP plus Fabric skills |
|---|---|---|
| Context | Human-pasted snippets | Live model metadata and PBIP/PBIR files |
| Execution | Human copy-paste | Tool calls and file edits |
| Scope | DAX snippets and advice | Semantic model plus report layer |
| Validation | Manual error feedback | DAX, schema, Desktop reload, screenshots |
| Git review | Often invisible | Plain-text TMDL and PBIR diffs |

Raw prompting is still useful for brainstorming. MCP and Fabric skills are the production authoring loop.
