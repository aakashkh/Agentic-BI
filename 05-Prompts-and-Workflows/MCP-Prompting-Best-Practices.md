# Power BI MCP Server Prompting Best Practices & Sample Playbook

This playbook provides **4 Golden Rules** and **5 tested prompt templates** for effectively prompting the **Microsoft Power BI Modeling MCP Server** (`@microsoft/powerbi-modeling-mcp`).

Following these practices prevents Copilot/AI agents from hanging in recursive schema loops and ensures **3-second execution times** for all TMDL model operations.

---

## 1. Why Prompts Hang (And How to Fix It)

### The Problem:
If an AI agent or Copilot runs for 5+ minutes when connected to an MCP server, it has entered a **recursive tool loop**. This happens when a prompt is too broad or vague (e.g., *"add a few columns and measures"*), causing the agent to repeatedly call `pbi_get_schema` without knowing which table file to modify.

### The Fix:
1. Click **Stop / Cancel (Square Icon)** in the Copilot chat window (or press `Ctrl + C` in terminal).
2. Re-issue an **atomic, targeted prompt** that explicitly names the target table (`SalesMetrics`, `FactSales`, `DimCustomer`).

---

## 2. The 4 Golden Rules of Prompting Power BI MCP Servers

```
  Rule 1: Always Specify Target Table  ➔  "Target table: SalesMetrics.tmdl"
  Rule 2: Inspect First, Modify Second ➔  1. pbi_get_schema  ➔  2. pbi_add_measure
  Rule 3: Provide DAX + Format String  ➔  Format: "0.00%", Folder: "Time Intelligence"
  Rule 4: Atomic Prompts (1 task/prompt)➔  Don't request 10 tables at once
```

1. **Always Name the Target Table**: Specify the exact table `.tmdl` file (`SalesMetrics`, `FactSales`, `DimCustomer`).
2. **2-Step Execution (Inspect ➔ Modify)**:
   - *Step 1*: `"Inspect schema of FactSales table using pbi_get_schema."`
   - *Step 2*: `"Now add [YoY Sales Growth %] measure to SalesMetrics."`
3. **Specify DAX, Format Strings & Display Folders**: Give explicit formatting rules so MCP doesn't guess (`0.00%` or `$#,0.00`).
4. **Keep Prompts Atomic**: Request one measure or one table update per prompt. Do not ask for 10 columns across 5 tables in a single prompt.

---

## 3. 5 Ready-to-Use Sample Prompts (Tested & Fast)

### Template 1: Adding a Time-Intelligence Measure (YoY Growth %)
> *"Using `pbi_add_measure`, add a measure named `'YoY Sales Growth %'` to the `'SalesMetrics'` table.*  
> *DAX formula:*  
> `VAR CurrentSales = [Total Sales]`  
> `VAR PriorSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('DimDate'[Date]))`  
> `RETURN DIVIDE(CurrentSales - PriorSales, PriorSales, 0)`  
> *Format string: `0.00%`, Display folder: `Time Intelligence`, Description: `'Year-over-Year Sales Growth percentage calculation.'`"*

---

### Template 2: Auto-Documenting TMDL Table Columns
> *"Using `pbi_update_description`, add business documentation comments (`///`) to the `'FactSales'` table.*  
> *Set description for `'OrderDate'` to `'Date when customer order was placed'` and `'SalesAmount'` to `'Total gross sales revenue before discounts.'`"*

---

### Template 3: Schema Inspection Before DAX Creation
> *"Execute `pbi_get_schema` on `./03-Demo-Project/RetailSales.pbip` and list all existing measures inside the `'SalesMetrics'` table."*

---

### Template 4: Validating TMDL Model & DAX Dependencies
> *"Run `pbi_validate_tmdl` on `./03-Demo-Project/RetailSales.pbip` to check for syntax errors or broken table relationships."*

---

### Template 5: Cross-Model Measure Copying
> *"Using `pbi_copy_object`, copy the measure `'Sales YTD'` from source model `./ReferenceModel.pbip` into target table `'SalesMetrics'` in `./03-Demo-Project/RetailSales.pbip`."*

---

## 4. Quick Comparison Guide

| ❌ Vague Prompt (Avoid - Causes 10-min hangs) | ✅ Targeted MCP Prompt (Recommended - 3-sec execution) |
| :--- | :--- |
| *"Add a few columns and measures to my model."* | *"Add a measure `Total Sales` = `SUM(FactSales[SalesAmount])` to table `SalesMetrics` with format string `$#,0.00`."* |
| *"Fix my Power BI model."* | *"Run `pbi_validate_tmdl` on `./03-Demo-Project/RetailSales.pbip` and list syntax errors."* |
| *"Document everything."* | *"Use `pbi_update_description` to add business documentation to `FactSales[SalesAmount]`."* |
