# Agentic Business Intelligence — Team Guide & Workshop Suite

Welcome to the **Agentic Business Intelligence (Agentic BI)** repository! This workspace contains the complete hands-on material, live demo project, prompt playbooks, architecture guides, and interactive slide deck for the 90-minute workshop: **"Agentic Business Intelligence — Build a Thinking Dashboard with Power BI MCP + PBIP"**.

---

## 🧭 How Team Members Can Use This Workspace Right Now

Follow this 4-step walkthrough to explore and run the codebase before session planning next week:

### Step 1: Open the Interactive Presentation Deck & Read the Technical Article
Explore the 18-slide interactive presentation with light/dark theme toggling and click-to-expand full-screen diagrams, or read the Medium-style technical publication:
* ✍️ **Medium Technical Article**: [`02-Presentation/Medium-Blog-Post.md`](02-Presentation/Medium-Blog-Post.md)
* 📄 **Interactive Slide Deck**: [`02-Presentation/Agentic_BI_Slides.html`](file:///c:/Users/aakashkhandelwal/Downloads/Learning/Agentic%20BI/02-Presentation/Agentic_BI_Slides.html)
* 📖 **Slide Outline & Visual Maps**: [`02-Presentation/Slide-Deck-Outline.md`](02-Presentation/Slide-Deck-Outline.md)
* 💡 **PBIX GUI ➔ PBIP Folder Parallel Guide**: [`02-Presentation/PBIX-to-PBIP-Mapping-Guide.md`](02-Presentation/PBIX-to-PBIP-Mapping-Guide.md)

---

### Step 2: Open & Test the TMDL Power BI Project (`RetailSales.pbip`)
The demo project is formatted in **TMDL (Tabular Model Definition Language)** text files and populated with **5,000 synthetic retail transactions** (2023–2026):
1. Launch **Power BI Desktop** (August 2026 release or later).
2. Open [`03-Demo-Project/RetailSales.pbip`](03-Demo-Project/RetailSales.pbip).
3. Click **Refresh** in the ribbon to load data directly from [`03-Demo-Project/Data/*.csv`](03-Demo-Project/Data/).
4. Inspect TMDL files directly in VS Code under [`03-Demo-Project/RetailSales.Dataset/definition/tables/`](03-Demo-Project/RetailSales.Dataset/definition/tables/).

---

### Step 3: Install & Enable Power BI Modeling MCP Server via Plugin
Install **Microsoft Power BI Modeling MCP Server via Plugin** (in Plugins Manager UI or via `agy plugin install powerbi-modeling`), rather than installing a standard VS Code extension:
* 🔌 **Plugin Installation Guide**: [`04-MCP-Setup/mcp-config-guide.md`](04-MCP-Setup/mcp-config-guide.md)
* 📄 **Workspace Plugin Config**: [`04-MCP-Setup/mcp-server-config.json`](04-MCP-Setup/mcp-server-config.json)
* 🧪 **Standalone Python MCP Simulator**: Run `python 04-MCP-Setup/mock-mcp-simulator.py` to test TMDL tool calls offline.

---

### Step 4: Practice Prompt Playbooks & CI/CD Review Gates
Use pre-tested prompt templates to generate DAX measures, document TMDL schema, and test Git PR gates:
* 🧮 **DAX Generation Playbook**: [`05-Prompts-and-Workflows/DAX-Generation-Playbook.md`](05-Prompts-and-Workflows/DAX-Generation-Playbook.md)
* 📝 **Auto-Documentation Playbook**: [`05-Prompts-and-Workflows/Documentation-Playbook.md`](05-Prompts-and-Workflows/Documentation-Playbook.md)
* 🌉 **Fabric Data Agent Readiness Bridge**: [`05-Prompts-and-Workflows/Fabric-Data-Agent-Bridge.md`](05-Prompts-and-Workflows/Fabric-Data-Agent-Bridge.md)
* 📋 **Cross-Model Copy Playbook**: [`05-Prompts-and-Workflows/Cross-Model-Copy-Playbook.md`](05-Prompts-and-Workflows/Cross-Model-Copy-Playbook.md)
* 🛡️ **Git PR Review & Azure DevOps CI Gate**: [`05-Prompts-and-Workflows/PR-Review-Gate.md`](05-Prompts-and-Workflows/PR-Review-Gate.md)

---

## 📁 Complete Repository Directory Layout

```
Agentic BI/
├── README.md                           # Master team navigation guide (This document)
├── 01-Session-Plan/                    # Workshop Facilitation Materials
│   ├── 90-Min-Agenda.md               # Minute-by-minute timeline (Modules 1 to 5)
│   └── Facilitator-Guide.md            # Speaker transition notes, setup checklist & troubleshooting FAQs
├── 02-Presentation/                    # Presentation & Architecture Visuals
│   ├── Medium-Blog-Post.md             # Medium-style technical publication article
│   ├── Agentic_BI_Slides.html          # Interactive 18-slide deck (Light/Dark theme + Fullscreen Lightbox)
│   ├── PowerBI-CI-CD-and-Deployment-Pipelines-Architecture.md # Deep-dive Fabric CI/CD & Deployment Pipelines Guide
│   ├── PBIX-to-PBIP-Mapping-Guide.md   # Side-by-side Desktop GUI ➔ TMDL parallel mapping guide
│   ├── Slide-Deck-Outline.md          # 18-slide detailed outline with visual maps
│   ├── Key-Concepts.md                 # Deep dive into PBIP schemas, TMDL comments & CI/CD
│   └── images/                         # 10 clean high-resolution presentation visual assets
│       ├── dual_agent_continuum.jpg    # Slide 1: Authoring Agent vs Consumption Agent hero visual
│       ├── git_pbix_vs_pbip_diff.jpg   # Slide 2: Git Versioning Diff - Binary PBIX vs Plain-Text TMDL
│       ├── pbip_folder_deep_dive.jpg   # Slide 3: PBIP Folder Hierarchy & Internal Schema Anatomy
│       ├── pbix_to_pbip_folder.jpg     # PBIX binary exploding into plain-text TMDL files
│       ├── mcp_architecture.jpg        # Power BI Modeling MCP protocol framework
│       ├── mcp_protocol_anatomy.jpg    # Slide 9: Model Context Protocol (MCP) Framework Anatomy
│       ├── mcp_vs_standard_prompts.jpg # Slide 9: MCP Tool Use vs Standard LLM Chat Prompts
│       ├── fabric_agent_tmdl.jpg       # Slide 10: Fabric Data Agent reasoning over TMDL annotations
│       ├── cicd_pipeline_gate.jpg      # Slide 14: Azure DevOps automated testing & PR gate
│       └── ecosystem_blueprint.jpg     # Slide 17 & 18: Linear 5-step enterprise lifecycle blueprint
├── 03-Demo-Project/                    # Live Power BI Project (PBIP) & Data
│   ├── RetailSales.pbip               # Validated root pointer file
│   ├── generate_data.py                # Synthetic dataset generator script
│   ├── Data/                           # Populated CSV data tables (5,000 transactions, 200 customers)
│   │   ├── FactSales.csv
│   │   ├── DimCustomer.csv
│   │   ├── DimProduct.csv
│   │   └── DimDate.csv
│   ├── RetailSales.Report/             # Report definition folder (definition.pbir, report.json)
│   └── RetailSales.Dataset/            # Semantic model folder (definition.pbism, model.bim)
│       └── definition/
│           ├── model.tmdl              # Model config
│           ├── relationships.tmdl      # Star schema relationships
│           └── tables/                 # Table-level TMDL definitions
│               ├── FactSales.tmdl
│               ├── DimCustomer.tmdl
│               ├── DimProduct.tmdl
│               ├── DimDate.tmdl        # Tagged with dataCategory: Time
│               └── SalesMetrics.tmdl   # Disconnected measure container
├── 04-MCP-Setup/                       # Model Context Protocol Setup
│   ├── mcp-config-guide.md             # VS Code, Claude Desktop & Copilot configuration instructions
│   ├── mcp-server-config.json          # Production JSON config snippet for @microsoft/powerbi-modeling-mcp
│   └── mock-mcp-simulator.py           # Python simulation script for offline testing
└── 05-Prompts-and-Workflows/           # Prompt Engineering Playbooks & CI Gates
    ├── DAX-Generation-Playbook.md      # Natural language -> DAX measure templates
    ├── Documentation-Playbook.md       # Auto-documenting TMDL tables & columns
    ├── Fabric-Data-Agent-Bridge.md     # Metadata readiness checklist for Fabric Data Agents
    ├── Cross-Model-Copy-Playbook.md    # Headless TMDL measure copying across projects
    └── PR-Review-Gate.md               # Git PR review checklist & azure-pipelines.yml CI workflow
```

---

## 🧠 Core Architecture: The Dual-Agent Continuum

```
 ┌────────────────────────────────────────────────────────┐
 │                    AUTHORING AGENT                     │
 │      VS Code + Power BI MCP + PBIP (TMDL Files)        │
 │   • Builds DAX measures via natural language           │
 │   • Auto-documents tables, columns & business rules    │
 │   • Standardizes TMDL format & calculation groups      │
 └──────────────────────────┬─────────────────────────────┘
                            │ (Git PR & Azure DevOps CI/CD)
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │                   CONSUMPTION AGENT                    │
 │      Fabric Data Agent / Fabric Copilot in Service     │
 │   • Answers end-user Q&A in natural language           │
 │   • Generates dynamic DAX & data explorations          │
 │   • Grounded in TMDL triple-slash (///) annotations    │
 └────────────────────────────────────────────────────────┘
```

---

## 🔗 Official Microsoft Documentation & References

* 🛠️ **Power BI Modeling MCP Server GitHub Repo**: [`https://github.com/microsoft/powerbi-modeling-mcp`](https://github.com/microsoft/powerbi-modeling-mcp)
* 🔌 **Power BI MCP Servers Overview (MS Learn)**: [`https://learn.microsoft.com/en-us/power-bi/developer/mcp/mcp-servers-overview`](https://learn.microsoft.com/en-us/power-bi/developer/mcp/mcp-servers-overview)
* 📁 **Power BI Projects (.pbip) Developer Overview**: [`https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview`](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)
* 📜 **Tabular Model Definition Language (TMDL) Specification**: [`https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview`](https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview)
* 🖥️ **Use TMDL View in Power BI Desktop**: [`https://learn.microsoft.com/en-us/power-bi/transform-model/tmdl-view`](https://learn.microsoft.com/en-us/power-bi/transform-model/tmdl-view)
* 🚀 **Microsoft Fabric Git Integration Intro**: [`https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration`](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration)
* 🤖 **Fabric Data Agents & Copilot Overview**: [`https://learn.microsoft.com/en-us/fabric/get-started/copilot-fabric-overview`](https://learn.microsoft.com/en-us/fabric/get-started/copilot-fabric-overview)
* 📐 **Tabular Object Model (TOM) Developer Reference**: [`https://learn.microsoft.com/en-us/analysis-services/tom/introduction-to-tabular-object-model-tom-in-analysis-services-amo`](https://learn.microsoft.com/en-us/analysis-services/tom/introduction-to-tabular-object-model-tom-in-analysis-services-amo)
