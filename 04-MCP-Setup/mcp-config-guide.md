# Official Microsoft Power BI Modeling MCP Server — Plugin Installation & Setup Guide

> **IMPORTANT WORKSHOP INSTRUCTION**: In this workshop session, we install the **Microsoft Power BI Modeling MCP Server via Plugin** (Antigravity Plugins Manager / Plugin CLI) rather than a generic VS Code extension.

---

## 1. Step-by-Step Plugin Installation Instructions for Attendees

Follow these exact steps to install and enable the **Power BI Modeling MCP Server Plugin**:

### Method 1: Install via Plugins Manager UI (Recommended for Workshop Attendees)

1. **Open the Plugins Manager**:
   - Click on the **Plugins Manager** icon in the side panel of your AI IDE / Antigravity, or press `Ctrl + Shift + P` (`Cmd + Shift + P` on Mac) and select **Plugins: Open Plugins Manager**.
2. **Search for the Power BI Plugin**:
   - In the search box, enter: `Power BI Modeling` or `@microsoft/powerbi-modeling-mcp`.
3. **Install & Enable**:
   - Click the **Install** button next to **Microsoft Power BI Modeling MCP Plugin**.
   - Verify that the toggle status shows **Enabled** (Green indicator).
4. **Configure Project Path**:
   - When prompted for the project path, point it to your workshop PBIP folder:
     `c:/Users/aakashkhandelwal/Downloads/Learning/Agentic BI/03-Demo-Project/RetailSales.pbip` (or relative path `./03-Demo-Project/RetailSales.pbip`).

---

### Method 2: Install via Plugin CLI (`agy plugin`)

If you prefer installing via terminal command line:

```powershell
# 1. Search for available plugins
agy plugin search powerbi

# 2. Install the Power BI Modeling MCP Plugin
agy plugin install powerbi-modeling

# 3. Enable the plugin in your current workspace
agy plugin enable powerbi-modeling
```

---

### Method 3: Pre-Configured Workspace Plugin Manifest (`.vscode/plugins.json`)

If your workshop environment uses pre-configured plugin manifests, the server is declared in your workspace settings:

```json
{
  "plugins": [
    {
      "name": "powerbi-modeling-mcp",
      "package": "@microsoft/powerbi-modeling-mcp",
      "enabled": true,
      "settings": {
        "projectPath": "./03-Demo-Project/RetailSales.pbip"
      }
    }
  ]
}
```

---

## 2. Option B Fallback: Air-Gapped Python Stdio Simulator

For offline workshops without internet or plugin download permissions:

```json
{
  "mcpServers": {
    "powerbi-modeling-local": {
      "command": "python",
      "args": [
        "c:/Users/aakashkhandelwal/Downloads/Learning/Agentic BI/04-MCP-Setup/mock-mcp-simulator.py",
        "--pbip-root",
        "c:/Users/aakashkhandelwal/Downloads/Learning/Agentic BI/03-Demo-Project/RetailSales.pbip"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

---

## 3. Verifying Plugin Installation & Tool Availability

Once installed via Plugin, your AI Agent will automatically detect the 5 core Power BI modeling tools:

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| `pbi_get_schema` | `pbip_path` | Returns JSON hierarchy of tables, columns, measures, and relationships. |
| `pbi_add_measure` | `table`, `name`, `dax`, `formatString`, `displayFolder`, `description` | Injects DAX measure with triple-slash (`///`) documentation into TMDL. |
| `pbi_update_description` | `target_type`, `target_name`, `description` | Updates TMDL documentation comments. |
| `pbi_validate_tmdl` | `pbip_path` | Validates TMDL syntax and measure dependency trees. |
| `pbi_copy_object` | `source_pbip`, `target_pbip`, `object_type`, `object_name` | Ports TMDL snippets across semantic models. |

To verify in chat, simply ask your agent:
> *"List available tools from the Power BI Modeling Plugin."*
