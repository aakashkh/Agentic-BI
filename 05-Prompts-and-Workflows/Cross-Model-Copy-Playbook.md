# Cross-Model TMDL Copying Playbook

This playbook demonstrates how AI Agents copy DAX measures, calculation groups, and dimension tables across different PBIP projects without opening Power BI Desktop.

---

## 1. Scenario: Copying Standard Time Intelligence Suite

**Context**: You have a standardized Time Intelligence measure library in a reference project (`CorporateKPIs.pbip`) and want to port it to `RetailSales.pbip`.

---

## 2. Prompt Template

```text
Act as a Power BI Automation Engineer.

Target Source: `CorporateKPIs.pbip` (Reference Library)
Target Destination: `RetailSales.pbip` (`SalesMetrics.tmdl`)

Perform the following headless TMDL operations:
1. Extract the `[YoY Sales Growth %]` and `[Sales YTD]` measure definitions from the reference project.
2. Adapt the source table references to match `RetailSales` (`FactSales[SalesAmount]` and `DimDate[Date]`).
3. Inject the adapted measures into `RetailSales.Dataset/definition/tables/SalesMetrics.tmdl`.
4. Validate that lineageTags are uniquely regenerated.
```

---

## 3. TMDL Copying Benefits

* **No GUI Locking**: Copy calculation groups or DAX tables across 20 PBIP repositories in seconds.
* **Standardized Corporate KPIs**: Enforce corporate DAX formulas (e.g., EBITDA, ARR, Churn %) across distinct line-of-business models.
