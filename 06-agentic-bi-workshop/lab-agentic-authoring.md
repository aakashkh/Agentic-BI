# Workshop Exercise: Add Time Intelligence and a PBIR Visual

This lab uses the existing `RetailSales.pbix` as the source and asks an agent to perform a full authoring loop:

1. Convert the PBIX into a new PBIP/PBIR working copy.
2. Add time-intelligence measures through the Power BI Authoring MCP server.
3. Add a report page and visual block through the `powerbi-report-authoring` skill.
4. Validate the model, PBIR files, and Desktop rendering.

Do not modify `../03-Demo-Project`.

---

## Lab Goal

Create a new `Sales Trend` report page with:

- `Total Sales`
- `Sales Previous Year`
- `Sales YoY Amount`
- `Sales YoY %`
- A line chart comparing current sales to previous-year sales by date.
- KPI cards for total sales and YoY percentage.
- A date slicer.

---

## Starting Point

Source file:

```text
../03-Demo-Project/RetailSales.pbix
```

Existing semantic model:

```text
FactSales
DimDate
DimProduct
DimCustomer
SalesMetrics
```

Existing date relationship:

```text
FactSales[OrderDate] -> DimDate[Date]
```

Existing measure container:

```text
SalesMetrics
```

---

## Step 1: Create a Workshop Copy

In Power BI Desktop September 2026 or later:

1. Open `../03-Demo-Project/RetailSales.pbix`.
2. Select `File > Save as`.
3. Choose `Power BI Project (*.pbip)`.
4. Save to:

```text
06-agentic-bi-workshop/work/RetailSales-Agentic/
```

5. Open the saved `.pbip` from the new working folder.
6. Save once more so Desktop writes the current project files to disk.

Expected result:

```text
06-agentic-bi-workshop/work/RetailSales-Agentic/
├── RetailSales-Agentic.pbip
├── RetailSales-Agentic.Dataset/
└── RetailSales-Agentic.Report/
```

---

## Step 2: Start the Agent Environment

Open `06-agentic-bi-workshop` in VS Code, then start Copilot interactive skills mode from the repository root:

```bash
copilot -i skills
```

If the Copilot banner says a newer runtime has downloaded, run:

```text
/restart
```

Then confirm:

```text
/skills
```

Expected:

- `powerbi-report-authoring` is listed.
- The plugin-provided `powerbi-modeling-mcp` MCP server is available.

If Copilot reports that `powerbi-modeling-mcp` is defined by multiple plugin bundles, open `/plugin` and keep only the focused `powerbi-authoring@fabric-collection` bundle for this lab. Use the manual `powerbi-authoring-local` fallback only if the plugin route is unavailable. If this is the first run, accept the Power BI MCP EULA only after reviewing it.

---

## Step 3: Connect to the Model

Use one of these prompts.

For an open Power BI Desktop session:

```text
Connect to 'RetailSales-Agentic' in Power BI Desktop.
List the tables, relationships, and existing measures. Do not make changes yet.
```

For file-based authoring:

```text
Open semantic model from PBIP folder 'C:\Users\aakashkhandelwal\Downloads\Learning\Agentic BI\06-agentic-bi-workshop\work\RetailSales-Agentic\RetailSales-Agentic.Dataset\definition'.
List the tables, relationships, and existing measures. Do not make changes yet.
```

Check that the agent reports:

- `FactSales`
- `DimDate`
- `DimProduct`
- `DimCustomer`
- `SalesMetrics`
- The `FactSales[OrderDate]` to `DimDate[Date]` relationship

---

## Step 4: Add Time-Intelligence Measures

Prompt the agent:

```text
Using the Power BI Authoring MCP server, add these measures to the SalesMetrics table in the connected RetailSales-Agentic semantic model.

1. Total Sales = SUM(FactSales[SalesAmount])
2. Sales Previous Year = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(DimDate[Date]))
3. Sales YoY Amount = [Total Sales] - [Sales Previous Year]
4. Sales YoY % = DIVIDE([Sales YoY Amount], [Sales Previous Year])

Use currency formatting for the first three measures and percentage formatting for Sales YoY %. Add clear descriptions for each measure. Validate the DAX before committing the changes.
```

Expected agent behavior:

- Uses MCP `measure_operations`, not raw file guessing.
- Creates or updates measures in `SalesMetrics`.
- Sets format strings.
- Adds descriptions.
- Validates DAX against the model.
- Reports any model ambiguity before writing.

Instructor note:

If the agent detects that `DimDate` is not marked as a date table, ask it to inspect the date column metadata and recommend the minimal model change before proceeding. Do not let it create hidden auto date tables.

---

## Step 5: Validate Measures

Prompt:

```text
Run a small validation query by year that returns DimDate[Year], Total Sales, Sales Previous Year, Sales YoY Amount, and Sales YoY %. Limit the result to the most recent five years.
```

Expected:

- The query succeeds.
- The first year may have blank previous-year values.
- Later years show previous-year and YoY values.

If validation fails, ask the agent to explain the failure and repair the measure definitions through MCP.

---

## Step 6: Add a PBIR Report Page and Visual Block

Prompt:

```text
Using the powerbi-report-authoring skill, edit the PBIR report files in the RetailSales-Agentic.Report folder. Create a new page named Sales Trend.

Add:
- A page title text box: Sales Trend
- A line chart with DimDate[Date] on the X axis and SalesMetrics[Total Sales] plus SalesMetrics[Sales Previous Year] as values.
- A card for SalesMetrics[Total Sales].
- A card for SalesMetrics[Sales YoY %].
- A date slicer using DimDate[Date].

Use a clean business dashboard layout, keep all visuals within the canvas, and validate the PBIR schema after editing. Do not alter the source files under ../03-Demo-Project.
```

Expected agent behavior:

- Uses the report authoring skill for PBIR mechanics.
- Creates or updates files under `RetailSales-Agentic.Report/definition/pages/`.
- Creates one folder per visual.
- Writes schema-correct `page.json` and `visual.json` files.
- Runs `validate-report` if the skill exposes it.
- Reloads Power BI Desktop or asks the learner to apply external changes.

---

## Step 7: Review in Desktop

In Power BI Desktop:

1. Apply external changes if prompted.
2. Open the `Sales Trend` page.
3. Confirm the line chart, KPI cards, and slicer render.
4. Save the project.

If Desktop shows an error icon on a visual, prompt:

```text
Diagnose the Sales Trend page visual error. Inspect the PBIR visual bindings and queryState, validate against the report schema, and repair the smallest set of files needed.
```

---

## Step 8: Review the Git Diff

Run:

```bash
git diff -- 06-agentic-bi-workshop/work/RetailSales-Agentic
```

Expected diff categories:

- TMDL updates in the semantic model for the new measures.
- PBIR JSON files for the new page and visuals.
- No changes under `03-Demo-Project`.

Review checklist:

- Measure names are business-readable.
- DAX uses the model's actual table and column names.
- Formatting and descriptions are present.
- PBIR visuals reference existing fields and measures.
- No generated cache files are committed.

---

## Completion Criteria

The lab is complete when:

- The model includes all four time-intelligence measures.
- DAX validation succeeds.
- The `Sales Trend` page renders in Power BI Desktop.
- The PBIR files validate.
- The Git diff is understandable and limited to the workshop working copy.
- `../03-Demo-Project` remains unchanged.
