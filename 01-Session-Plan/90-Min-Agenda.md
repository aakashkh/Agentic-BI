# 90-Minute Session Agenda & Script

**Session Title**: Agentic Business Intelligence — Build a Thinking Dashboard with Power BI MCP + PBIP  
**Total Duration**: 90 Minutes  
**Session Delivery Style**: Interactive Presentation (25%) + Live Demo & Hands-on Coding (75%)

---

## Detailed Minute-by-Minute Timeline

```
┌─────────┬──────────────────────────────────────────────────────────┬───────────┐
│ Time    │ Module Name                                              │ Format    │
├─────────┼──────────────────────────────────────────────────────────┼───────────┤
│ 00-15m  │ Module 1: The Agentic BI Paradigm & PBIP Shift           │ Keynote   │
│ 15-30m  │ Module 2: Connecting the Power BI Modeling MCP Server    │ Hands-on  │
│ 30-65m  │ Module 3: Hands-on Agentic Modeling (DAX & Docs)         │ Workshop  │
│ 65-80m  │ Module 4: Fabric Data Agent Hook & Headless TMDL Ops     │ Live Demo │
│ 80-90m  │ Module 5: Git PR Quality Gate, Best Practices & Q&A      │ Interactive│
└─────────┴──────────────────────────────────────────────────────────┴───────────┘
```

---

### Module 1: The Agentic BI Paradigm & PBIP Shift (00:00 - 00:15)
* **Goal**: Reframe BI from desktop GUI clicking to code-first semantic engineering.
* **Key Topics**:
  * PBIX binary limits: Why merge conflicts, lack of code review, and GUI locking block AI automation.
  * What is PBIP & TMDL? Plain-text Tabular Model Definition Language.
  * The Dual-Agent Architecture:
    * **Authoring Agent**: Developer's co-pilot in VS Code via MCP.
    * **Consumption Agent**: Fabric Data Agent / Fabric Copilot for business end-users.
* **Facilitator Action**:
  * Open `RetailSales.pbip` directory in VS Code alongside a traditional `.pbix` file.
  * Show `definition/tables/FactSales.tmdl` to prove it is 100% human- and agent-readable text.

---

### Module 2: Connecting the Power BI Modeling MCP Server (00:15 - 00:30)
* **Goal**: Get every participant connected to their local PBIP TMDL model via Model Context Protocol.
* **Key Topics**:
  * What is MCP (Model Context Protocol)? Standardizing tool calls between LLMs and local dev environments.
  * Configuring `mcp-server-config.json` in VS Code / Claude / Copilot / Antigravity.
  * Inspecting available tools: `get_model_schema`, `add_dax_measure`, `update_tmdl_description`, `validate_tmdl`.
* **Hands-on Exercise**:
  * Participants verify MCP server status by running: `"List all tables in RetailSales dataset"` via agent prompt.

---

### Module 3: Hands-on Agentic Modeling (00:30 - 01:05)
* **Goal**: Build real DAX measures and auto-document the model through natural language.
* **Exercise 3A: Prompt-Driven DAX Creation (15 mins)**
  * Prompt 1: *"Create a measure `Total Sales Amount` in `SalesMetrics` calculating sum of `FactSales[SalesAmount]`."*
  * Prompt 2: *"Create a `YoY Sales Growth %` time-intelligence measure using `DimDate[Date]`, with `DIVIDE` safety handling."*
  * Prompt 3: *"Add a `Gross Margin Target Attainment %` calculated metric."*
* **Exercise 3B: Automated TMDL Documentation (15 mins)**
  * Prompt: *"Scan all columns in `FactSales` and measures in `SalesMetrics`. Add TMDL `description` properties in business English and compile a standalone `Data-Dictionary.md` file."*
* **Facilitator Action**:
  * Highlight how TMDL files update in real-time in VS Code Git diff view.

---

### Module 4: Fabric Data Agent Hook & Headless Operations (01:05 - 01:20)
* **Goal**: Show how rich TMDL metadata activates Fabric Data Agents, and demonstrate headless BI.
* **Key Topics**:
  * **The Fabric Data Agent Hook**: Explain that when this PBIP project is deployed to Microsoft Fabric workspace/capacity, Fabric Data Agents rely directly on the TMDL descriptions and measures created in Module 3.
  * Demonstration: *"Garbage TMDL in = Hallucinated Fabric Data Agent out"*.
  * **Headless BI**: Show editing TMDL files without opening Power BI Desktop GUI (demonstrating cross-platform dev on Mac/Linux/Cloud containers).

---

### Module 5: Git PR Quality Gate, Best Practices & Q&A (01:20 - 01:30)
* **Goal**: Establish the repeatable production pattern: Git branch -> Agent co-authoring -> PR code review -> Automated CI deployment.
* **Key Topics**:
  * Opening a Pull Request on GitHub with agent-authored TMDL code.
  * Running Best Practice Analyzer (BPA) checks on TMDL syntax.
  * Reviewing DAX code formatting and safety rules in Git diff view.
* **Closing Q&A**: Taking attendee questions and providing takeaway links.
