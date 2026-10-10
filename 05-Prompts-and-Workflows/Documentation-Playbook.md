# Automated TMDL Documentation & Data Dictionary Playbook

This playbook demonstrates how AI Agents scan TMDL semantic models, auto-document tables, columns, and measures with triple-slash (`///`) comments, and export a Markdown `Data-Dictionary.md` file.

---

## Prompt 1: In-Place TMDL Auto-Documentation

```text
Act as a Data Catalog & Governance Specialist.
Scan all TMDL files in `RetailSales.Dataset/definition/tables/`.

For every table, column, and measure:
1. Infer its business purpose from table relationships and column names.
2. Inject a clear, concise 1-sentence TMDL triple-slash (`///`) comment above the object definition.
3. Ensure no existing code or formatting is altered.

Example Target TMDL Output:
/// Physical customer master table containing demographics and customer segmentations
table DimCustomer
	/// Unique primary identifier for customer accounts
	column CustomerID
```

---

## Prompt 2: Compiling Standalone Markdown Data Dictionary

```text
Inspect all TMDL files in `RetailSales.Dataset/definition/tables/`.
Extract all tables, columns, measures, data types, format strings, and descriptions.

Generate a comprehensive standalone `Data-Dictionary.md` file in the root directory.

Format the output as follows:
# Retail Sales Semantic Model - Data Dictionary

## Table: FactSales
| Object Name | Type | Data Type | Format String | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SalesAmount` | Column | Decimal | \$#,0.00 | Total gross sales revenue in USD. |
| `Total Sales Amount` | Measure | Decimal | \$#,0.00 | Sum of sales revenue across selected context. |
```
