# Power BI MCP Server Prompting Best Practices & Methodology

This guide provides the **4 Golden Rules** and foundational prompt anatomy for prompting the **Microsoft Power BI Modeling MCP Server** (`@microsoft/powerbi-modeling-mcp`).

Following these practices prevents Copilot/AI agents from hanging in recursive schema loops and ensures **sub-5-second execution times** for all TMDL model operations.

---

## 1. Why Prompts Hang (And How to Fix It)

### The Problem:
If an AI agent or Copilot runs for 5–10+ minutes when connected to an MCP server, it has entered a **recursive tool loop**. This happens when a prompt is broad or ambiguous (e.g., *"add a few columns and measures"*), causing the agent to repeatedly call schema inspection tools without knowing which table file or partition to mutate.

### The Immediate Fix:
1. Click **Stop / Cancel (Square Icon)** in the Copilot chat window (or press `Ctrl + C` in the terminal).
2. Re-issue an **atomic, targeted prompt** that explicitly names the target table (`SalesMetrics.tmdl`, `FactSales.tmdl`, `DimCustomer.tmdl`).

---

## 2. The 4 Golden Rules of Power BI MCP Prompting

```
  Rule 1: Always Specify Target Table  ➔  "Target table: SalesMetrics.tmdl"
  Rule 2: Inspect First, Modify Second ➔  1. get_table_schema  ➔  2. create_measure
  Rule 3: Provide DAX + Format String  ➔  Format: "0.00%", Folder: "Time Intelligence"
  Rule 4: Keep Prompts Atomic (1 task) ➔  1 measure or 1 table at a time
```

1. **Always Name the Target Table**: Specify the exact table name or `.tmdl` file path (`SalesMetrics`, `FactSales`, `DimDate`).
2. **2-Step Execution (Inspect First, Modify Second)**:
   - *Step 1*: `"Inspect schema of FactSales and DimDate using get_table_schema."`
   - *Step 2*: `"Now create [YoY Sales Growth %] measure in SalesMetrics table."`
3. **Specify DAX Formula, Format Strings & Display Folders**: Give explicit formatting rules (`0.00%`, `$#,0.00`) so the agent doesn't guess.
4. **Keep Prompts Atomic**: Request one measure or one table update per turn. Avoid asking for multiple tables simultaneously in a single prompt.

---

## 3. Official MCP Tool Nomenclature Reference

The official Microsoft Power BI Modeling MCP Server (`@microsoft/powerbi-modeling-mcp`) exposes the following core tools:

| MCP Tool Name | Action | Parameters |
| :--- | :--- | :--- |
| `powerbi_modeling:list_tables` | Lists all tables in the dataset | `projectPath` |
| `powerbi_modeling:get_table_schema` | Returns columns, measures & partitions of a table | `tableName`, `projectPath` |
| `powerbi_modeling:create_measure` | Creates a new DAX measure in TMDL | `tableName`, `measureName`, `expression`, `formatString`, `displayFolder`, `description` |
| `powerbi_modeling:update_description` | Adds triple-slash (`///`) documentation | `tableName`, `objectName`, `description` |
| `powerbi_modeling:validate_model` | Validates TMDL syntax & relationships | `projectPath` |

---

## 4. Foundational Prompt Templates

### Template 1: Safe 2-Step Schema Inspection
```text
Execute `powerbi_modeling:get_table_schema` on table "SalesMetrics" in `./03-Demo-Project/RetailSales.pbip`.
List all existing measures and their display folders before proceeding.
```

### Template 2: Single-Measure Creation (Atomic & Fast)
```text
Using `powerbi_modeling:create_measure`, add the following measure to the "SalesMetrics" table:
- Measure Name: "YoY Sales Growth %"
- Expression:
  VAR CurrentSales = [Total Sales]
  VAR PriorSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('DimDate'[Date]))
  RETURN DIVIDE(CurrentSales - PriorSales, PriorSales, 0)
- Format String: "0.0%"
- Display Folder: "Time Intelligence"
- Description: "Year-over-Year percentage growth in Total Sales."
```

### Template 3: Semantic Documentation (`///` Annotations)
```text
Using `powerbi_modeling:update_description`, update the "FactSales" table:
- Set description for column "SalesAmount" to: "Total gross sales revenue before tax and customer discounts in USD."
- Set description for column "OrderDate" to: "Date when customer order was placed, joining to DimDate[Date]."
```

---

## 5. Quick Comparison: Vague vs. Targeted Prompts

| ❌ Vague Prompt (Causes 10-min Hangs) | ✅ Targeted MCP Prompt (3-sec Execution) |
| :--- | :--- |
| *"Add a few columns and measures to my model."* | *"Add a measure `Total Sales` = `SUM(FactSales[SalesAmount])` to table `SalesMetrics` with format `$#,0.00`."* |
| *"Fix my Power BI model."* | *"Run `powerbi_modeling:validate_model` on `RetailSales.pbip` and list any syntax errors."* |
| *"Document everything in the database."* | *"Use `powerbi_modeling:update_description` to document columns in `FactSales.tmdl`."* |

---

## 📚 Specialized Prompt Playbooks in this Suite

For comprehensive prompt templates organized by engineering objective, refer to:
* 🧮 **DAX Generation & Performance Suite**: [`DAX-Generation-Playbook.md`](DAX-Generation-Playbook.md) (Base measures, Time Intelligence, VAR/RETURN refactoring)
* 📝 **Automated Catalog & Markdown Dictionary**: [`Documentation-Playbook.md`](Documentation-Playbook.md) (Batch TMDL documentation & `Data-Dictionary.md` generation)
* 🌉 **Fabric Data Agent Readiness**: [`Fabric-Data-Agent-Bridge.md`](Fabric-Data-Agent-Bridge.md) (TMDL semantic readiness checklist for Fabric Copilot)
* 📋 **Cross-Model Copying**: [`Cross-Model-Copy-Playbook.md`](Cross-Model-Copy-Playbook.md) (Headless copying of calculation groups & KPI suites)
* 🛡️ **Git PR Quality Gate**: [`PR-Review-Gate.md`](PR-Review-Gate.md) (Pull request checklist & CI pipeline setup)
