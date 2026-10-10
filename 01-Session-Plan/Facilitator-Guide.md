# Facilitator Guide & Delivery Playbook

**Session**: Agentic Business Intelligence — Build a Thinking Dashboard with Power BI MCP + PBIP  
**Target Audience**: BI Engineers, Data Architects, Analytics Engineers

---

## 1. Pre-Session Checklist (T-30 Minutes)

- [ ] Verify VS Code / AI IDE is installed with git extension.
- [ ] Confirm Plugin installation method: Instruct attendees to install **Microsoft Power BI Modeling MCP Server via Plugin** (Plugins Manager UI or `agy plugin install powerbi-modeling`), NOT via standard VS Code extension.
- [ ] Test the Power BI Modeling MCP Server / Simulator script (`04-MCP-Setup/mock-mcp-simulator.py`).
- [ ] Ensure `03-Demo-Project/RetailSales.pbip` opens cleanly in VS Code.
- [ ] Stage git repository with a clean `main` branch to demonstrate live TMDL git diffs.

---

## 2. Key Transitions & Speaker Notes

### Slide 1: The PBIX Bottleneck
> *"For 10 years, Power BI development meant one thing: opening a 500MB binary `.pbix` file in Power BI Desktop, clicking GUI buttons, and dreading git merge conflicts. AI models couldn't read binary files, so BI was left behind in the AI engineering revolution. PBIP and TMDL change that completely."*

### Slide 2: Authoring Agent vs. Consumption Agent (Fabric Data Agent)
> *"Every executive wants a Fabric Data Agent — a conversational AI that answers business questions over company data. But Fabric Data Agents don't magically know your business logic. If your semantic model has cryptic column names and no measure descriptions, the agent fails. That's why we focus on the **Authoring Agent**: using VS Code + MCP to build clean, documented TMDL code that makes Fabric Data Agents brilliant."*

### Slide 3: Live Demo Transition (VS Code)
> *"Watch my screen. I have no Power BI Desktop open. I'm looking at `FactSales.tmdl` in VS Code. I'm going to ask my AI co-developer to add a YoY Sales Growth measure and document the entire table. Watch how the `.tmdl` files update in real-time."*

---

## 3. Common Troubleshooting & FAQs

| Issue | Cause | Fix / Response |
| :--- | :--- | :--- |
| **MCP server connection failed** | Path or runtime mismatch in `mcp-server-config.json` | Use the standalone simulator script (`mock-mcp-simulator.py`) or verify Node/Python environment path. |
| **"Do I need Fabric Capacity to use this?"** | Misunderstanding of Authoring vs Consumption agents | *"No! PBIP, TMDL, and Power BI MCP run 100% locally in VS Code or Power BI Desktop free edition. Fabric capacity is only needed if you want to publish to Fabric Data Agents later."* |
| **"Can I edit TMDL without Power BI Desktop?"** | Question about Headless BI | *"Yes! TMDL is plain text. You can edit TMDL on Mac, Linux, or GitHub Codespaces, then deploy via Tabular Editor CLI or Fabric Git Integration."* |
| **"How do we prevent AI from generating bad DAX?"** | Governance / Accuracy concern | *"The PR is our quality gate. We run automated Best Practice Analyzer (BPA) checks in GitHub Actions and require human code review before merging."* |

---

## 4. Time Management & Fallbacks

- **If Module 2 (MCP Setup) runs long**: Direct attendees to run prompts against the `mock-mcp-simulator.py` script to keep pace.
- **If hands-on DAX generation finishes early**: Move into **Cross-Model Metric Copying** (`05-Prompts-and-Workflows/Cross-Model-Copy-Playbook.md`) to showcase copying calculation groups across semantic models.
