# Agentic BI Workshop: PBIX to PBIP, PBIR, MCP, and Fabric Skills

This module adds a September 2026 workshop track for migrating a local Power BI Desktop file into an agent-driven authoring workflow. It uses the existing `../03-Demo-Project/RetailSales.pbix` as the source artifact, but does not modify anything under `../03-Demo-Project`.

---

## What This Module Teaches

By the end of the lab, the learner can:

1. Convert a local `.pbix` file into a source-controlled Power BI Project (`.pbip`).
2. Explain how PBIR report files and TMDL semantic model files split the project into reviewable text.
3. Configure the local Power BI Authoring MCP server for semantic model work.
4. Install Skills for Fabric so an agent can edit PBIR report layout files.
5. Ask an agent to add time-intelligence measures and report visuals, then validate the result.

---

## September 2026 Baseline

Power BI Desktop projects (`.pbip`) and Power BI enhanced report format (`.pbir`) are now the baseline format for developer-mode Power BI work. PBIP saves a report and semantic model as folders of individual plain-text files, which makes Git diffs and code review meaningful.

The important September 2026 shift is:

- PBIR is generally available and is the default report format.
- Editing or saving older PBIR-Legacy reports silently converts them into PBIR.
- PBIR stores pages, visuals, bookmarks, report metadata, and layouts as granular JSON files.
- Semantic models are stored as TMDL text under the dataset or semantic model folder.
- Visual Studio Code can validate PBIR JSON against public schemas and can show pixel-level report changes in source control.

The current Microsoft documentation also notes that PBIP/PBIR external editing is GA, while automatic Desktop reload and the Desktop Bridge remain preview features. Treat reload automation as a workshop accelerator, not as a production dependency.

References:

- Power BI external project editing: https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-external-editing
- Power BI report folder and PBIR structure: https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report
- Power BI project overview: https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview

---

## The Split Architecture

Agentic Power BI authoring is not one giant tool. It is a split architecture.

### 1. Power BI Authoring MCP Server

The Power BI Authoring MCP Server is the semantic model tool surface. In the September 2026 workshop baseline, version `1.0.0` is the GA baseline: local `stdio` is GA, while the hosted remote endpoint is still preview.

Use it for:

- Tables
- Columns
- Relationships
- Measures
- DAX validation
- Object descriptions
- Bulk model refactoring
- TMDL-backed semantic model changes

Do not use it for:

- Report page layout
- Visual placement
- Themes
- PBIR visual JSON authoring
- Canvas or bookmark design

Local mode is the correct choice for this workshop because it can connect to Power BI Desktop and local PBIP files. Hosted mode is useful for Fabric workspace models, but it cannot reach local files on the learner's machine.

### 2. Skills for Fabric

Skills for Fabric are declarative agent instructions and tool workflows distributed through `microsoft/skills-for-fabric`. The focused Power BI bundle is `powerbi-authoring`.

Use the `powerbi-report-authoring` skill for:

- PBIR page JSON
- Visual JSON
- Layout and position updates
- Filters, slicers, formatting, and themes
- Schema-aware report validation
- Desktop Bridge reload and screenshot loops when available

The practical end-to-end loop is:

1. MCP server changes the semantic model.
2. `powerbi-report-authoring` skill edits the PBIR report layer.
3. The agent validates PBIR JSON schemas.
4. Power BI Desktop reloads the changed project.
5. The agent iterates until the model, report files, and rendered report agree.

References:

- Power BI Authoring MCP server: https://learn.microsoft.com/en-us/power-bi/developer/mcp/power-bi-authoring-mcp
- Power BI Report Authoring skill: https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-report-authoring-skill-overview
- Skills for Fabric install guide: https://learn.microsoft.com/en-us/fabric/fundamentals/skills-for-fabric-install
- Skills for Fabric GitHub repository: https://github.com/microsoft/skills-for-fabric

---

## Source Project Analysis

The primary source file for this workshop is:

```text
../03-Demo-Project/RetailSales.pbix
```

The demo project also includes an already-converted PBIP folder that learners can inspect:

```text
../03-Demo-Project/RetailSales.pbip
../03-Demo-Project/RetailSales.Dataset/
../03-Demo-Project/RetailSales.Report/
```

Treat these as read-only. For hands-on work, save a fresh workshop copy outside `../03-Demo-Project`, for example:

```text
06-agentic-bi-workshop/work/RetailSales-Agentic/
```

---

## Task A: Convert PBIX to PBIP and PBIR

Follow these steps in Power BI Desktop September 2026 or later.

1. Open Power BI Desktop.
2. Open `../03-Demo-Project/RetailSales.pbix`.
3. Select `File > Save as`.
4. Choose `Power BI Project (*.pbip)`.
5. Save into a new workshop working folder, not into `../03-Demo-Project`.
6. Use a short path to avoid the Windows 260-character project file path limit.
7. Confirm that Power BI Desktop created a `.pbip` file plus a `.Dataset` or `.SemanticModel` folder and a `.Report` folder.
8. Save the project before asking an agent to modify files externally.

September 2026 behavior:

- Saving the `.pbix` as `.pbip` creates source-controlled project files.
- The report layer is stored in PBIR.
- If the source report contains PBIR-Legacy metadata, saving or editing converts it to PBIR.
- The semantic model is stored as TMDL text files.

---

## Generated PBIP Architecture

A converted Retail Sales project should look like this:

```text
RetailSales-Agentic/
├── RetailSales-Agentic.pbip
├── .gitignore
├── RetailSales-Agentic.Dataset/
│   ├── definition.pbism
│   ├── item.config.json
│   └── definition/
│       ├── model.tmdl
│       ├── relationships.tmdl
│       └── tables/
│           ├── DimCustomer.tmdl
│           ├── DimDate.tmdl
│           ├── DimProduct.tmdl
│           ├── FactSales.tmdl
│           └── SalesMetrics.tmdl
└── RetailSales-Agentic.Report/
    ├── definition.pbir
    ├── item.config.json
    └── definition/
        ├── report.json
        ├── version.json
        ├── pages/
        │   ├── pages.json
        │   └── <pageName>/
        │       ├── page.json
        │       └── visuals/
        │           └── <visualName>/
        │               ├── visual.json
        │               └── mobile.json
        └── bookmarks/
            ├── bookmarks.json
            └── <bookmarkName>.bookmark.json
```

Key folders:

| Folder or file | Purpose | Agent role |
|---|---|---|
| `.pbip` | Pointer file that opens the report project in Power BI Desktop. | Used to open the project. Usually not hand-edited. |
| `.Dataset/definition/tables/*.tmdl` | Plain-text table, column, partition, and measure definitions. | MCP server reads and writes model metadata. |
| `.Dataset/definition/relationships.tmdl` | Model relationship definitions. | MCP server creates, validates, and updates relationships. |
| `.Report/definition.pbir` | Report metadata and dataset reference. | Usually generated by Desktop. |
| `.Report/definition/report.json` | Report-level PBIR metadata. | Read by report authoring tools and schemas. |
| `.Report/definition/pages/*/page.json` | Page metadata and canvas settings. | Edited by `powerbi-report-authoring`. |
| `.Report/definition/pages/*/visuals/*/visual.json` | One file per visual. | Edited by `powerbi-report-authoring`. This is where Git diffs become useful. |

The existing demo model contains these tables:

- `FactSales`
- `DimDate`
- `DimProduct`
- `DimCustomer`
- `SalesMetrics`

The existing relationships are:

- `FactSales[CustomerID]` to `DimCustomer[CustomerID]`
- `FactSales[ProductID]` to `DimProduct[ProductID]`
- `FactSales[OrderDate]` to `DimDate[Date]`

---

## Task B: Configure VS Code and Copilot

Use the clean install path in `clean-installation-guide.md` if this is your first time setting up the workshop. The short version is: install the focused `powerbi-authoring@fabric-collection` plugin and do not add a separate active `.vscode/mcp.json` for the same Power BI MCP server.

### Prerequisites

Install:

- Power BI Desktop September 2026 or later.
- VS Code with GitHub Copilot Chat.
- Node.js LTS, so `npx` can start the local MCP package.
- Git.
- An MCP-capable agent client in agent mode.

For Power BI Desktop external reload:

1. Open `File > Options and settings > Options > Preview features`.
2. Enable `Detect and reload external PBIP changes`.
3. Restart Power BI Desktop.

### Open Copilot Interactive Skills Mode

For this workshop, use Copilot's interactive terminal mode from the repository root:

```bash
copilot -i skills
```

You should see a Copilot terminal where slash commands such as `/plugin`, `/skills`, `/mcp`, `/restart`, and `? help` are available. If the terminal banner says that a newer Copilot version has downloaded, run `/restart` before configuring plugins so the session uses the current runtime.

### Install Skills for Fabric

Inside `copilot -i skills`, install the focused Power BI authoring bundle:

```text
/plugin marketplace add microsoft/skills-for-fabric
/plugin install powerbi-authoring@fabric-collection
/skills
```

Use the CLI-subcommand form only if your installation exposes plugin management outside interactive mode:

```bash
copilot plugin marketplace add microsoft/skills-for-fabric
copilot plugin install powerbi-authoring@fabric-collection
copilot skills
```

For this workshop, `powerbi-authoring` is required. The broader `fabric-skills` bundle is optional and can be useful later for Fabric workspace tasks, but do not install it during the first lab unless you need those broader skills. Some Copilot builds register `powerbi-modeling-mcp` from both `powerbi-authoring` and `fabric-skills`; installing both can produce a duplicate-server warning and tool routing ambiguity.

If you already installed both bundles and see duplicate MCP messages, open `/plugin` and disable or uninstall one of the overlapping bundles for the lab. Keep `powerbi-authoring@fabric-collection` when the task is local PBIP/PBIR authoring.

Expected skills after installation include:

- `powerbi-semantic-model-authoring`
- `powerbi-report-planner`
- `powerbi-report-design`
- `powerbi-report-authoring`
- `powerbi-report-management`

### Manual MCP Fallback Configuration

This module includes:

```text
06-agentic-bi-workshop/.vscode/mcp.local.example.json
```

This is intentionally an example file, not an active `.vscode/mcp.json`. For the default Copilot workshop path, the `powerbi-authoring@fabric-collection` plugin contributes the Power BI MCP server, so no project MCP file is needed.

Use the example only when your MCP client does not already register the plugin-provided Power BI MCP server. It registers the local Power BI Authoring MCP server over `stdio`:

```json
{
  "servers": {
    "powerbi-authoring-local": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@microsoft/powerbi-modeling-mcp@latest", "--start"]
    }
  }
}
```

If your MCP client uses the portable format, use a root `.mcp.json`, `mcpConfig.json`, or `.clauderc` shape like this:

```json
{
  "mcpServers": {
    "powerbi-authoring-local": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@microsoft/powerbi-modeling-mcp@latest", "--start"]
    }
  }
}
```

Some clients document the shorter package mapping below. Use it only if that client starts the package without the explicit `--start` argument:

```json
{
  "mcpServers": {
    "powerbi-authoring-local": {
      "command": "npx",
      "args": ["-y", "@microsoft/powerbi-modeling-mcp"]
    }
  }
}
```

Regulated or repeatable classroom environments can pin the GA `1.0.0` package:

```json
{
  "mcpServers": {
    "powerbi-authoring-local": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@microsoft/powerbi-modeling-mcp@1.0.0", "--start"]
    }
  }
}
```

Do not register the local and hosted Power BI Authoring MCP servers at the same time for this lab. They expose overlapping semantic model tools and can make tool routing ambiguous.

Also avoid two local registrations with the same tool purpose. If Copilot reports that `powerbi-modeling-mcp` is already defined by a plugin, prefer the plugin-provided server in Copilot and keep `.vscode/mcp.local.example.json` only as fallback documentation.

### EULA Handling

The first time the npm package starts, the server may require EULA acceptance. In an interactive workshop, let the agent call the `accept_eula` tool only after the learner explicitly agrees.

For unattended internal lab machines, an administrator can add `--accepteula` or set `PBI_MODELING_MCP_ACCEPT_EULA=true` after reviewing the EULA.

---

## Verification Workflow

Use this 3-step smoke test before the exercise.

### 1. Verify Fabric Skills

In `copilot -i skills`, run:

```text
/skills
```

Expected result:

- The Power BI authoring skills are listed.
- `powerbi-report-authoring` is present.
- The broader Fabric bundle appears only if you intentionally installed `fabric-skills`.

### 2. Verify Local MCP over stdio

In Copilot interactive mode, inspect the plugin-provided server:

```text
/mcp show powerbi-modeling-mcp
```

In VS Code, use the plugin-provided server in Copilot. If you are deliberately using the manual fallback, copy `.vscode/mcp.local.example.json` into a real `.vscode/mcp.json`, then start `powerbi-authoring-local` from the CodeLens or agent tools menu.

Then ask:

```text
Tell me with examples what I can do with the Power BI Authoring MCP server.
```

Expected result:

- The server starts as a local process through `npx`.
- The tool list includes semantic model operations such as tables, columns, measures, relationships, DAX query execution, and connection operations.
- If prompted, review and accept the EULA.

### Troubleshooting the Copilot Terminal

If the terminal shows:

```text
MCP server 'powerbi-modeling-mcp': also defined by plugin ...
```

then two installed plugin bundles are trying to contribute the same Power BI MCP server. Use `/plugin` to disable or remove one overlapping bundle. For this lab, keep `powerbi-authoring@fabric-collection`.

If the terminal shows:

```text
Failed to connect to MCP server "powerbi-modeling-mcp": ... FeatureNotAvailable
```

run `/mcp show powerbi-modeling-mcp` and check whether the failing registration is coming from the wrong plugin bundle or from a hosted/preview configuration. Prefer the local `stdio` server for this workshop.

If the terminal shows:

```text
Failed to load models: Error: 403 "unauthorized: not authorized to use this Copilot feature"
```

that is an account, token, or model-catalog issue, not a Power BI project-file issue. Do not reinstall the Power BI plugin first if `/mcp` still shows `Power BI Authoring MCP Server (Local)` from `powerbi-authoring`.

Use this reset sequence:

```text
/user
/logout
/login
/restart
/mcp
/skills
```

If the 403 clears after restart or re-login, the setup was already correct. Continue with the lab.

### 3. Verify Desktop or PBIP Connection

Open the saved workshop PBIP in Power BI Desktop, then ask:

```text
Connect to 'RetailSales-Agentic' in Power BI Desktop.
List the tables, relationships, and measures in the connected semantic model.
```

If you are working from files instead of a running Desktop session, ask:

```text
Open semantic model from PBIP folder 'C:\Users\aakashkhandelwal\Downloads\Learning\Agentic BI\06-agentic-bi-workshop\work\RetailSales-Agentic\RetailSales-Agentic.Dataset\definition'.
List the tables, relationships, and measures in the model.
```

Expected result:

- The agent can see `FactSales`, `DimDate`, `DimProduct`, `DimCustomer`, and `SalesMetrics`.
- The agent can read the `FactSales` relationships.
- A read-only request succeeds before any write operation is attempted.

---

## Workshop Files

This folder contains:

```text
06-agentic-bi-workshop/
├── README.md
├── clean-installation-guide.md
├── lab-agentic-authoring.md
├── mcp-vs-raw-prompting.md
├── .copilot/
│   └── instructions.md
└── .vscode/
    ├── mcp.local.example.json
    └── settings.json
```

Use `clean-installation-guide.md` for setup decisions, `lab-agentic-authoring.md` for the practical exercise, and `mcp-vs-raw-prompting.md` for the conceptual comparison.

---

## Safety Rules for the Lab

- Do not edit `../03-Demo-Project`.
- Save a workshop copy before allowing an agent to write changes.
- Save Power BI Desktop before editing files externally.
- Apply or discard Power BI Desktop external-change prompts before continuing.
- Commit a clean baseline before the agent starts.
- Review Git diffs before accepting the completed report.
- Use the MCP server for semantic model changes.
- Use `powerbi-report-authoring` for PBIR report layout changes.
