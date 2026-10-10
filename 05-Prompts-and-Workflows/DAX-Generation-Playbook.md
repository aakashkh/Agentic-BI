# DAX Generation & Refactoring Playbook

This playbook provides natural language prompt templates for creating, refactoring, and optimizing DAX measures directly in TMDL files using an AI Agent via MCP.

---

## Prompt 1: Base Business Metrics Creation

**Objective**: Create fundamental aggregation measures in the `SalesMetrics` table.

```text
Act as a Senior Power BI DAX Engineer. 
Inspect the `RetailSales.Dataset` TMDL model. 
Create the following base measures in the `SalesMetrics` table:

1. `Total Sales Amount`: Sum of `FactSales[SalesAmount]`, formatted as currency (\$#,0.00).
2. `Total Quantity Sold`: Sum of `FactSales[Quantity]`, formatted as integer (#,0).
3. `Average Order Value`: Total Sales Amount divided by distinct count of `FactSales[TransactionID]`, with DIVIDE safety, formatted as currency.

Add proper `displayFolder: Base Metrics` and business descriptions (`///`) for each measure in TMDL.
```

---

## Prompt 2: Time Intelligence Measures

**Objective**: Generate robust YoY and YTD time intelligence calculations linked to `DimDate`.

```text
Act as a Power BI DAX Specialist.
In `SalesMetrics.tmdl`, create a time intelligence suite based on `[Total Sales Amount]` and `DimDate[Date]`:

1. `Sales YTD`: YTD Total Sales Amount using TOTALYTD.
2. `Sales Prior Year`: Sales amount for the same period last year using SAMEPERIODLASTYEAR.
3. `YoY Sales Growth Amount`: `[Total Sales Amount] - [Sales Prior Year]`.
4. `YoY Sales Growth %`: `DIVIDE([YoY Sales Growth Amount], [Sales Prior Year], 0)`, formatted as 0.00%.

Ensure all measures are placed in `displayFolder: Time Intelligence` and include TMDL documentation comments explaining the calculation logic.
```

---

## Prompt 3: Performance Optimization & Refactoring

**Objective**: Refactor raw DAX measures to eliminate implicit measures and improve performance.

```text
Analyze all measures in `SalesMetrics.tmdl`.
Check for the following performance anti-patterns:
- Use of FILTER(ALL(...)) instead of KEEPFILTERS or REMOVEFILTERS.
- Missing DIVIDE error protection.
- Lack of variables (VAR/RETURN) for repeated sub-expressions.

Refactor any inefficient measures and write the updated TMDL code back to `SalesMetrics.tmdl`.
```
