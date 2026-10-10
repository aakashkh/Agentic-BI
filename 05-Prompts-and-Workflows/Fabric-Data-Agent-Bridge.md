# Fabric Data Agent Readiness Bridge

This guide outlines how authoring TMDL metadata via an AI Agent in VS Code directly enables **Fabric Data Agents** (Consumption Agents) in Microsoft Fabric.

---

## 1. The Architectural Link

```
┌────────────────────────────────────────────────────────────────────────┐
│                      AUTHORING PHASE (VS Code)                         │
│  Authoring Agent (Power BI MCP) enriches TMDL with:                    │
│  • Triple-slash descriptions (///)                                     │
│  • Business-friendly display names & display folders                   │
│  • Standardized DAX measure expressions & format strings               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Fabric Git Sync / CI/CD)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     CONSUMPTION PHASE (Fabric Service)                 │
│  Fabric Data Agent uses enriched TMDL metadata to:                     │
│  • Interpret natural language business questions accurately            │
│  • Route queries to the correct tables and DAX measures                │
│  • Avoid hallucinated joins or incorrect aggregation formulas           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Fabric Data Agent Readiness Checklist

Before publishing your PBIP dataset to a Fabric workspace for Fabric Data Agent consumption, verify the following metadata standards in TMDL:

- [ ] **Table Descriptions**: Every table has a `///` description explaining its granularity.
- [ ] **Column Business Names**: Avoid database abbreviations (e.g., use `Customer Segment` instead of `c_seg_cd`).
- [ ] **Explicit Measures Only**: Set `defaultPowerBIDataSourceVersion` and hide raw numeric fact columns to prevent implicit SUM measures.
- [ ] **Data Category Annotations**: Explicitly tag `dataCategory: Time` on `DimDate` and geography categories on location columns.
- [ ] **Synonym Annotations**: Add synonyms in TMDL for common business phrasing (e.g., "Revenue" -> `[Total Sales Amount]`).

---

## 3. Fabric Data Agent Readiness Evaluation Prompt

```text
Act as a Microsoft Fabric AI Architect.
Inspect `RetailSales.Dataset` TMDL files.
Evaluate our semantic model's readiness for Fabric Data Agent Q&A.

Generate a "Fabric Data Agent Readiness Report" assessing:
1. Metadata Coverage: Percentage of columns and measures with `///` descriptions.
2. Measure Exposure: Are raw fact numeric columns hidden?
3. Naming Clarity: Are column names business-friendly?

Output recommendations for TMDL updates to optimize Fabric Data Agent query accuracy.
```
