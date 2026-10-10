# PBIX GUI to PBIP/TMDL Folder Mapping Guide

**Target Audience**: BI Developers, Data Analysts, and Power BI Engineers transitioning from `.pbix` GUI button-clicking to code-first `.pbip` TMDL semantic modeling in Git.

---

## The Mental Shift: Where Did My PBIX Go?

In traditional `.pbix`, all model elements (tables, relationships, measures, M queries, RLS roles) are saved together inside a single compressed binary blob. 

In `.pbip`, your semantic model lives inside `RetailSales.Dataset/definition/` decomposed into clean, human-readable text files:

```
RetailSales.Dataset/definition/
├── model.tmdl                     # [1] Model Settings & Ref Pointers
├── relationships.tmdl             # [2] Relationship View
├── tables/                        # [3] Data View & Fields Pane
│   ├── FactSales.tmdl             #     Table columns, measures & M query partition
│   ├── DimCustomer.tmdl           #     Table columns & M query partition
│   ├── DimProduct.tmdl            #     Table columns & M query partition
│   ├── DimDate.tmdl               #     Marked Date Table & Calendar columns
│   └── SalesMetrics.tmdl          #     Measure Container Table
├── roles/                         # [4] Manage Roles (RLS DAX Filters)
│   └── RegionalManager.tmdl       #     Row-Level Security rules
├── cultures/                      # [5] Translations & Multi-Language
│   └── en-US.tmdl                 #     Localized display names
└── perspectives/                  # [6] Model Perspectives
    └── ExecutiveView.tmdl         #     Filtered sub-views of large models
```

---

## Parallel Comparison Table: PBIX Desktop GUI vs. PBIP/TMDL Code

| What you do in PBIX Desktop GUI | Where it lives in `RetailSales.Dataset/definition/` | TMDL Code Representation |
| :--- | :--- | :--- |
| **Model View ➔ Drag-and-drop relationship between tables** | `relationships.tmdl` | `relationship Rel_FactSales_DimCustomer`<br>`  fromColumn: FactSales.CustomerID`<br>`  toColumn: DimCustomer.CustomerID` |
| **Fields Pane ➔ Right click table ➔ New Measure** | `definition/tables/[TableName].tmdl` | `measure 'Total Sales' = SUM(FactSales[SalesAmount])`<br>`  formatString: \$#,0.00`<br>`  displayFolder: Base Metrics` |
| **Transform Data ➔ Power Query M Editor** | Inside `definition/tables/[TableName].tmdl` under `partition` | `partition FactSales-Partition = m`<br>`  mode: import`<br>`  source = let Source = Csv.Document(...)` |
| **Modeling Tab ➔ Manage Roles (RLS)** | `definition/roles/[RoleName].tmdl` | `role RegionalManager`<br>`  tablePermission DimCustomer`<br>`  filterExpression: DimCustomer[Country] = "USA"` |
| **Modeling Tab ➔ Mark as Date Table** | Inside `definition/tables/DimDate.tmdl` | `table DimDate`<br>`  dataCategory: Time`<br>`  column Date`<br>`    isKey` |
| **Properties Pane ➔ Display Folders & Format Strings** | Inside `definition/tables/[TableName].tmdl` under measure | `displayFolder: Time Intelligence`<br>`formatString: 0.00%` |
| **Data View ➔ Column Data Type & Summarization** | Inside `definition/tables/[TableName].tmdl` under column | `column Quantity`<br>`  dataType: int64`<br>`  summarizeBy: sum` |
| **Model View ➔ Triple-Slash Description** | Above object in `definition/tables/[TableName].tmdl` | `/// Sum of gross revenue in USD`<br>`measure 'Total Sales' = ...` |

---

## Detailed TMDL File Deep-Dives

### 1. `relationships.tmdl` (The Model Diagram View)
Instead of searching for lines on a canvas diagram, all relationships are listed textually:

```tmdl
relationship Rel_FactSales_DimCustomer
	fromColumn: FactSales.CustomerID
	toColumn: DimCustomer.CustomerID

relationship Rel_FactSales_DimDate
	fromColumn: FactSales.OrderDate
	toColumn: DimDate.Date
	crossFilteringBehavior: singleDirection
```

---

### 2. `tables/[TableName].tmdl` (Data View + DAX + Power Query M combined!)
Each table file is 3-in-1: it holds column data types, DAX measures, and the Power Query M import query!

```tmdl
table FactSales
	lineageTag: 11111111-2222-3333-4444-555555555555

	/// Column metadata
	column SalesAmount
		dataType: decimal
		sourceColumn: SalesAmount
		formatString: \$#,0.00

	/// DAX Measure definition
	/// Sum of total gross sales revenue in USD
	measure 'Total Sales' = SUM(FactSales[SalesAmount])
		formatString: \$#,0.00
		displayFolder: Base Metrics

	/// Power Query M partition code
	partition FactSales-Partition = m
		mode: import
		source = 
			let
			    Source = Csv.Document(File.Contents("Data/FactSales.csv"), [Delimiter=",", Columns=8]),
			    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
			in
			    #"Promoted Headers"
```

---

### 3. `roles/[RoleName].tmdl` (Manage Roles / RLS)
Row-Level Security rules are isolated into clear text files per security role:

```tmdl
role EuropeSalesManager
	lineageTag: 77777777-8888-9999-0000-111111111111

	tablePermission DimCustomer
		filterExpression: DimCustomer[Country] = "United Kingdom" || DimCustomer[Country] = "Germany"
```

---

## Why Developers Love This Folder Structure
1. **Targeted Git Diffs**: If you edit a DAX measure in `SalesMetrics.tmdl`, Git *only* tracks changes to `SalesMetrics.tmdl`. The rest of the model is untouched!
2. **Parallel Team Development**: Developer A can build new measures in `SalesMetrics.tmdl` while Developer B updates Power Query M code in `FactSales.tmdl` without merge conflicts!
3. **Instant Search**: Search across all DAX measures, column names, or M queries using VS Code `Ctrl+Shift+F`.
