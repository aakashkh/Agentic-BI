# Presentation Slide Deck Outline & Visual Map (16 Slides)

**Workshop Title**: Agentic Business Intelligence — Build a Thinking Dashboard with Power BI MCP + PBIP  
**Target Slide Count**: 16 Slides  
**Interactive Slide File**: [`02-Presentation/Agentic_BI_Slides.html`](file:///c:/Users/aakashkhandelwal/Downloads/Learning/Agentic%20BI/02-Presentation/Agentic_BI_Slides.html)

---

## Detailed Slide Breakdown

### Slide 1: Title & Hook
- **Title**: Agentic Business Intelligence
- **Subtitle**: Build a Thinking Dashboard with Microsoft Power BI MCP + PBIP
- **Tagline**: *Business Intelligence is getting an upgrade it didn't ask for — and it starts with a file format.*

---

### Slide 2: The PBIX Bottleneck (Why Binary Files Block AI)
- **The Old World**: Locked binary `.pbix` zip files, GUI clicking, unreviewable PRs, merge conflict nightmares.
- **The Solution**: PBIP + TMDL plain-text files natively in Git.

---

### Slide 3: PBIP Directory & File Hierarchy (Interactive Tree)
- Interactive inspector breaking down:
  - `RetailSales.pbip`
  - `RetailSales.Report/` (`definition.pbir`, `definition/report.json`, `item.config.json`)
  - `RetailSales.Dataset/` (`definition.pbism`, `model.bim`, `definition/tables/*.tmdl`, `item.config.json`)
  - `.cache/` & `.pbi/` (`cache.abf`, `localSettings.json`)

---

### Slide 4: PBIP JSON Schemas & Metadata Specifications
- `$schema` regex requirements enforced by Power BI Desktop.
- `item.config.json` GUID `logicalId` persistent identity tracking in Fabric Git.
- Bi-directional sync between `model.bim` (TMSL) and `.tmdl` files.

---

### Slide 5: TMDL Syntax Anatomy & Triple-Slash Comments
- YAML-like indentation hierarchy.
- Triple-slash (`///`) documentation mapping to description metadata.
- Multi-line VAR/RETURN DAX syntax.

---

### Slide 6: The `.cache` Aspect & `.gitignore` Rules
- **`cache.abf`**: Local Analysis Services database compressed data cache.
- **`localSettings.json`**: Developer-specific connection strings & credentials.
- **Security & Version Control Warning**: Why committing `.cache` bloats Git repositories and risks data exposure.

---

### Slide 7: The Dual-Agent Continuum (Authoring vs. Consumption)
- **Authoring Agent**: VS Code + Microsoft Power BI MCP Server + TMDL.
- **Consumption Agent**: Fabric Data Agent / Fabric Copilot in Microsoft Fabric workspace.
- **Golden Rule**: *Fabric Data Agents are only as smart as your TMDL metadata.*

---

### Slide 8: Official Microsoft Power BI Modeling MCP Server
- Package: `@microsoft/powerbi-modeling-mcp`
- Exposed tools: `pbi_get_schema`, `pbi_add_measure`, `pbi_update_description`, `pbi_validate_tmdl`, `pbi_copy_object`.

---

### Slide 9: Fabric Data Agent Readiness Calculator (Interactive Widget)
- Interactive assessment scoring TMDL metadata quality (`///` comments, business column names, hidden fact columns, time intelligence tagging).

---

### Slide 10: Live Workshop Hands-On Workflow
- 4-step hands-on roadmap: Open PBIP ➔ Connect MCP ➔ Prompt DAX ➔ Auto-document.

---

### Slide 11: Headless BI: Platform Independence & Reusability
- Cross-platform modeling on macOS, Linux, Codespaces.
- Reusing KPI measure suites across 10+ PBIP repositories.

---

### Slide 12: Fabric Git Integration & Azure DevOps Architecture
- Connecting Azure Repos / GitHub branches directly to Fabric Workspaces.
- Auto-syncing `main` branch TMDL changes to published semantic models.

---

### Slide 13: Azure DevOps CI/CD Pipelines for Power BI
- Automated YAML pipeline (`azure-pipelines.yml`).
- Steps: TMDL syntax validation ➔ Tabular Editor Best Practice Analyzer (BPA) ➔ Automated PR build gates.

---

### Slide 14: Fabric Deployment Pipelines (Dev ➔ Test ➔ Prod)
- **Dev Workspace**: Feature branch TMDL authoring.
- **Test Workspace**: Regression testing over full staging data.
- **Prod Workspace**: Zero-downtime production model serving business users and Fabric Data Agents.

---

### Slide 15: Interactive Agent Prompt Simulator
- Live interactive prompt runner demonstrating real-time TMDL modifications.

---

### Slide 16: The One Repeatable Blueprint & Takeaways
```
Semantic Model in Git → Agent as Co-Developer → PR Gate & Azure Pipelines → Deploy to Fabric
```
