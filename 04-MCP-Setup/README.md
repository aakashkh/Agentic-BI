# Power BI Modeling MCP walkthrough

This folder contains an isolated copy of the Retail Sales PBIP project with example semantic-model changes made through Power BI Modeling MCP. The original project in `03-Demo-Project` was not modified.

## Project contents

- [RetailSales-MCP-Demo/RetailSales.pbip](./RetailSales-MCP-Demo/RetailSales.pbip) — copied report project
- `RetailSales-MCP-Demo/RetailSales.SemanticModel/definition` — semantic-model TMDL, including the MCP changes
- `RetailSales-MCP-Demo/RetailSales.Report` — copied report definition
- `RetailSales-MCP-Demo/Data` — CSV files used by the model

## What changed

The starting model had five tables and three active, one-to-many relationships, with no explicit measures. The copied model now includes:

### Calculated columns on `DimDate`

| Column | DAX expression | Data type |
|---|---|---|
| `Year Month` | `FORMAT('DimDate'[Date], "yyyy-MM")` | String |
| `Month Start Date` | `DATE(YEAR('DimDate'[Date]), MONTH('DimDate'[Date]), 1)` | DateTime |

### Measures on `FactSales`

| Measure | DAX expression | Format |
|---|---|---|
| `Sales Amount` | `SUM('FactSales'[SalesAmount])` | `$#,##0.00` |
| `Units Sold` | `SUM('FactSales'[Quantity])` | `#,##0` |
| `Transaction Count` | `DISTINCTCOUNT('FactSales'[TransactionID])` | `#,##0` |

The aggregated base columns `FactSales[SalesAmount]` and `FactSales[Quantity]` are hidden so the measures are the user-facing fields.

## Follow along with MCP

Use the Power BI Modeling MCP tools. The operation names below are the MCP operations; the tool names are shown in backticks.

1. **Connect to the copied semantic model.** Use `connection_operations` with `operation: "ConnectFolder"` and this folder:

   ```text
   04-MCP-Setup\RetailSales-MCP-Demo\RetailSales.SemanticModel
   ```

   The server resolves the PBIP `definition` folder. Check the returned connection name and use it for subsequent calls.

2. **Inspect before editing.**

   - `table_operations` → `List`, then `GetSchema` for the relevant tables.
   - `relationship_operations` → `List`.
   - `measure_operations` → `List`.

3. **Add calculated columns.** Use `column_operations` → `Create` with `definitions` containing a `tableName`, `name`, `dataType`, and DAX `expression`. For example:

   ```json
   {
     "name": "Year Month",
     "tableName": "DimDate",
     "dataType": "String",
     "expression": "FORMAT('DimDate'[Date], \"yyyy-MM\")",
     "summarizeBy": "None"
   }
   ```

   Add `Month Start Date` using the expression in the table above, with `dataType: "DateTime"`, `formatString: "yyyy-mm-dd"`, and `summarizeBy: "None"`.

4. **Add explicit measures.** Use `measure_operations` → `Create`. Each definition needs `name`, `tableName`, and `expression`; set a suitable `formatString` and description as well. For example:

   ```json
   {
     "name": "Sales Amount",
     "tableName": "FactSales",
     "expression": "SUM('FactSales'[SalesAmount])",
     "formatString": "$#,##0.00"
   }
   ```

   Repeat for `Units Sold` and `Transaction Count` using the expressions above.

5. **Hide aggregated base columns.** Use `column_operations` → `Update` for `FactSales[SalesAmount]` and `FactSales[Quantity]`, setting `isHidden: true`. This keeps the explicit measures as the intended interface for report authors.

6. **Keep the copy independent.** The original model's CSV partitions used absolute paths into `03-Demo-Project\Data`. In this copy, each CSV-backed partition's `File.Contents` path points to the matching file under `RetailSales-MCP-Demo\Data`. If you move the project, update these paths (or replace them with a parameterized source) before refreshing.

7. **Persist MCP edits.** Use `database_operations` → `ExportToTmdlFolder` and set `tmdlFolderPath` to the PBIP definition folder:

   ```text
   04-MCP-Setup\RetailSales-MCP-Demo\RetailSales.SemanticModel\definition
   ```

   Exporting to the semantic-model folder's parent instead can put TMDL files beside `definition` rather than inside it; use the `definition` path for a PBIP project.

8. **Verify after export.** Reconnect with `ConnectFolder`, then check:

   - `table_operations` → `GetSchema` for `DimDate` and `FactSales`
   - `measure_operations` → `List`
   - `partition_operations` → `Get` to confirm the CSV paths point into the copied project

## Validation note

The copied TMDL reloaded successfully through MCP with five tables, three measures, and three relationships. The calculated columns are reported as ready. This is an offline TMDL connection, so MCP DAX query validation/execution is not supported here. Open the copied PBIP in Power BI Desktop, refresh if needed, and validate the measures against the live model with:

```dax
EVALUATE
ROW(
    "Sales Amount", [Sales Amount],
    "Units Sold", [Units Sold],
    "Transaction Count", [Transaction Count]
)
```
