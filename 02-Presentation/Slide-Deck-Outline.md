# Presentation Slide Deck Outline & Visual Map (18 Slides)

**Workshop Title**: Agentic Business Intelligence — Build a Thinking Dashboard with Power BI MCP + PBIP  
**Total Slide Count**: 18 Slides  
**Interactive Slide File**: [`02-Presentation/Agentic_BI_Slides.html`](Agentic_BI_Slides.html)  
**Interactive Screencast Player**: [`02-Presentation/demo-screencast.html`](demo-screencast.html)

---

## Detailed 18-Slide Breakdown

### Slide 1: Title & Hook
- **Title**: Agentic Business Intelligence
- **Subtitle**: Build a Thinking Dashboard with Microsoft Power BI MCP + PBIP
- **Tagline**: *Business Intelligence is getting an upgrade it didn't ask for — and it starts with a file format.*
- **Visual Asset**: Hero visual [`images/dual_agent_continuum.jpg`](images/dual_agent_continuum.jpg)

---

### Slide 2: The PBIX Bottleneck (Why Binary Files Block AI)
- **The Old World**: Locked binary `.pbix` zip blobs, GUI clicking, unreviewable PRs ("Binary files differ"), merge conflict nightmares.
- **The Modern Reality**: AI agents cannot parse or mutate binary blobs.
- **The Solution**: PBIP + TMDL plain-text files natively version-controlled in Git.
- **Visual Asset**: Side-by-side Git diff comparison [`images/git_pbix_vs_pbip_diff.jpg`](images/git_pbix_vs_pbip_diff.jpg)

---

### Slide 3: PBIP Directory & File Hierarchy (Interactive Tree)
- Interactive inspector breaking down:
  - `RetailSales.pbip` (Root pointer)
  - `RetailSales.Report/` (`definition.pbir`, `definition/report.json`, `item.config.json`)
  - `RetailSales.Dataset/` (`definition.pbism`, `model.bim`, `definition/tables/*.tmdl`, `item.config.json`)
  - `.cache/` & `.pbi/` (`cache.abf`, `localSettings.json`)
- **Visual Asset**: Deep-dive anatomy [`images/pbip_folder_deep_dive.jpg`](images/pbip_folder_deep_dive.jpg) and [`images/pbix_to_pbip_folder.jpg`](images/pbix_to_pbip_folder.jpg)

---

### Slide 4: PBIX Desktop GUI vs. PBIP TMDL Parallel Map (Rosetta Stone)
- Interactive tabs mapping common desktop actions directly to TMDL files:
  1. Model View drag-and-drop ➔ `relationships.tmdl`
  2. Fields pane "New Measure" ➔ `definition/tables/[Table].tmdl`
  3. Transform Data (M Query) ➔ `partition = m` in table TMDL
  4. Manage Roles (RLS) ➔ `roles/[Role].tmdl`
  5. Mark as Date Table ➔ `dataCategory: Time` in `DimDate.tmdl`

---

### Slide 5: PBIP JSON Schemas & Metadata Specifications
- `$schema` regex requirements enforced by Power BI Desktop engine.
- `definition.pbir`: Relative path pointing to semantic model (`../RetailSales.Dataset`).
- `definition.pbism`: Semantic model artifact boundary definition.
- `item.config.json`: Persistent `logicalId` GUID tracking across Git branches.

---

### Slide 6: TMDL Syntax Anatomy & Triple-Slash Comments
- YAML-like indentation hierarchy replacing verbose XMLA/TMSL.
- Triple-slash (`///`) documentation mapping to description metadata.
- Multi-line `VAR`/`RETURN` DAX syntax with explicit format strings and display folders.

---

### Slide 7: The `.cache` Aspect & `.gitignore` Rules
- **`cache.abf`**: Local Analysis Services database compressed binary data cache.
- **`localSettings.json`**: Developer-specific credentials, window states, and privacy levels.
- **Security & Version Control Warning**: Why committing `.cache` bloats Git repositories and leaks confidential data rows. Standard `.gitignore` rules.

---

### Slide 8: The Dual-Agent Continuum (Authoring vs. Consumption)
- **Authoring Agent**: VS Code + Power BI Modeling MCP Server + TMDL (Developer Co-Pilot).
- **Consumption Agent**: Fabric Data Agent / Fabric Copilot in Microsoft Fabric workspace.
- **The Golden Rule**: *Fabric Data Agents are only as smart as your TMDL metadata. Authoring agents enrich metadata so consumption agents deliver zero-hallucination answers.*

---

### Slide 9: Microsoft Power BI Modeling MCP Server Architecture
- Package: `@microsoft/powerbi-modeling-mcp` (connected via Plugin).
- Core tools: `list_tables`, `get_table_schema`, `create_measure`, `update_measure`, `validate_tmdl`.
- How MCP replaces fragile text generation with atomic, validated Tabular Object Model (TOM) tool execution.
- **Visual Assets**: [`images/mcp_protocol_anatomy.jpg`](images/mcp_protocol_anatomy.jpg) and [`images/mcp_vs_standard_prompts.jpg`](images/mcp_vs_standard_prompts.jpg)

---

### Slide 10: Fabric Data Agent Readiness Calculator (Interactive Widget)
- Interactive assessment scoring TMDL metadata quality:
  - Table & Measure `///` descriptions (+30%)
  - Clean business column names (+25%)
  - Hidden numeric fact columns (+25%)
  - Date table `dataCategory: Time` (+20%)
- Live readiness score rendering (0% - 100%).
- **Visual Asset**: Fabric Data Agent reasoning [`images/fabric_agent_tmdl.jpg`](images/fabric_agent_tmdl.jpg)

---

### Slide 11: Live Workshop Hands-On Workflow & Screencast
- 4-step hands-on roadmap: Open PBIP ➔ Connect MCP ➔ Prompt DAX ➔ Auto-document.
- **Live Demo Screencast Card**: Embedded thumbnail with click-to-expand high-res lightbox and one-click button to launch [`demo-screencast.html`](demo-screencast.html).
- **Visual Asset**: [`images/mcp_live_demo_screencast.jpg`](images/mcp_live_demo_screencast.jpg)

---

### Slide 12: Headless BI: Platform Independence & Reusability
- Cross-platform modeling on macOS, Linux, and GitHub Codespaces without running Power BI Desktop `.exe`.
- Reusing standard KPI suites across 10+ PBIP repositories via prompt-driven copying.
- Programmatic batch refactoring of DAX measures.

---

### Slide 13: Fabric Git Integration & Azure DevOps Architecture
- Connecting Azure Repos / GitHub branches directly to Fabric Workspaces.
- Bi-directional sync: Feature branch PRs sync directly to Fabric development workspaces.

---

### Slide 14: Azure DevOps CI/CD Pipelines for Power BI
- Automated YAML pipeline (`azure-pipelines.yml`).
- Pipeline steps: TMDL syntax validation ➔ Tabular Editor Best Practice Analyzer (BPA) ➔ Automated PR build gates.
- **Visual Asset**: Automated CI quality gate [`images/cicd_pipeline_gate.jpg`](images/cicd_pipeline_gate.jpg)

---

### Slide 15: Fabric Deployment Pipelines (Dev ➔ Test ➔ Prod)
- **Dev Workspace**: Feature branch TMDL authoring & fast iteration.
- **Test Workspace**: Regression testing over staging data with parameter rules.
- **Prod Workspace**: High-availability production model serving business users and Fabric Data Agents.

---

### Slide 16: Interactive Agent Prompt Simulator
- Live interactive prompt runner demonstrating real-time TMDL modifications:
  - Base aggregations (`Total Sales`)
  - Time intelligence (`YoY Sales Growth %`)
  - Auto-documentation (`///` description injection)

---

### Slide 17: The Enterprise Ecosystem Blueprint
- 5-step end-to-end lifecycle:
  1. *Authoring*: VS Code + Power BI MCP
  2. *Version Control*: Git Branches & Line-by-Line PRs
  3. *CI Validation*: Tabular Editor BPA & DAX Rules
  4. *Fabric Promotion*: Deployment Pipelines (Dev ➔ Test ➔ Prod)
  5. *Autonomous Consumption*: Fabric Data Agents Q&A
- **Visual Asset**: [`images/ecosystem_blueprint.jpg`](images/ecosystem_blueprint.jpg)

---

### Slide 18: Wrap-Up, References & Key Takeaways
- Master review of the core principles.
- Direct links to official Microsoft documentation, GitHub repos, and community resources.
