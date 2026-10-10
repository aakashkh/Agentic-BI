# Clean Installation Guide

Use this guide when the setup feels overloaded. The clean workshop path is:

```text
VS Code + Copilot CLI
        |
        v
powerbi-authoring plugin
        |
        +-- Power BI skills
        +-- local powerbi-modeling-mcp server
```

Do not start by installing a separate Power BI MCP extension, project `.mcp.json`, and multiple Fabric plugins. Add those only when you need a specific fallback.

---

## Recommended Workshop Install

Install once on the machine:

1. Power BI Desktop September 2026 or later.
2. VS Code.
3. GitHub Copilot extension for VS Code.
4. GitHub Copilot CLI.
5. Node.js LTS.
6. Git.

Then install one Copilot plugin:

```bash
copilot -i skills
```

Inside Copilot interactive mode:

```text
/plugin marketplace add microsoft/skills-for-fabric
/plugin install powerbi-authoring@fabric-collection
/restart
/skills
/mcp show powerbi-modeling-mcp
```

That is the default workshop setup.

---

## What Each Layer Means

| Layer | What it is | Scope | Use it in this workshop? |
|---|---|---|---|
| VS Code extension | The UI/client capability in VS Code, such as GitHub Copilot Chat or a Power BI MCP extension. | User or VS Code profile. | Yes for GitHub Copilot. Do not add a separate Power BI MCP extension unless the plugin path fails. |
| Marketplace plugin | A Copilot plugin installed from `microsoft/skills-for-fabric`. | Copilot user environment. | Yes: install `powerbi-authoring@fabric-collection`. |
| Skills | Instructions and workflows loaded by the plugin, such as semantic-model and report-authoring skills. | Usually user-level through the plugin; available when the plugin is active. | Yes, but install through the plugin, not manually. |
| MCP JSON | Manual tool-server registration in `.mcp.json`, `.vscode/mcp.json`, or `~/.copilot/mcp-config.json`. | Project or user, depending on file location. | No for the default path. Use only as fallback. |
| `fabric-skills` plugin | Broad Fabric engineering skill bundle. | Copilot user environment. | Optional later. Skip for the first local Power BI lab. |

---

## Power BI Plugin vs Fabric Plugin

Use `powerbi-authoring@fabric-collection` when you are doing:

- PBIX to PBIP conversion workflows.
- Local Power BI Desktop authoring.
- PBIP or TMDL files on disk.
- Semantic model authoring.
- PBIR report authoring.

Use `fabric-skills@fabric-collection` later when you are doing broader Fabric work:

- Fabric workspace automation.
- Lakehouse, warehouse, notebook, or pipeline tasks.
- End-to-end Fabric environment orchestration.

Microsoft documentation often says to install both for full coverage. That is true for a broad Fabric workstation. For this focused local workshop, install only `powerbi-authoring` first. It reduces duplicate MCP warnings and keeps tool routing simple.

---

## Global vs Project-Specific

| Item | Global/user-specific | Project-specific |
|---|---|---|
| VS Code extension install | Yes. Installed for the user or profile. | No, unless the repo only recommends it. |
| Copilot CLI install | Yes. Installed on the machine/user path. | No. |
| Copilot marketplace plugin install | Yes. Installed into the Copilot user environment. | No. |
| Skills from a plugin | Mostly user/global through that plugin. | They may act on the current project, but the install is not stored in the project. |
| `.vscode/settings.json` | Can be global or project. | In this module it is project-specific scaffolding. |
| `.vscode/mcp.json` | Can be project-specific. | Avoid active use here because the plugin already registers MCP. |
| `.mcp.json` at repo root | No. | Yes. Portable project MCP config. Use only if not using the plugin. |
| `~/.copilot/mcp-config.json` | Yes. | No. Avoid for classroom labs unless every project needs the same server. |

---

## Fallback: Manual MCP Only

Use manual MCP config only if the plugin cannot be used, or if you are testing another MCP-capable client.

This module includes an inactive example:

```text
06-agentic-bi-workshop/.vscode/mcp.local.example.json
```

To use it, copy its contents into a real `.vscode/mcp.json` or a portable `.mcp.json`. Do not do this while the `powerbi-authoring` plugin is already contributing `powerbi-modeling-mcp`.

Portable workspace fallback:

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

---

## Troubleshooting

If you see:

```text
MCP server 'powerbi-modeling-mcp': also defined by plugin ...
```

you have overlapping registrations. Keep `powerbi-authoring@fabric-collection` for this lab and disable the other overlapping plugin or manual MCP registration.

If you see:

```text
Failed to connect to MCP server "powerbi-modeling-mcp": ... FeatureNotAvailable
```

inspect the active MCP entry:

```text
/mcp show powerbi-modeling-mcp
```

Prefer the local plugin-provided server for this workshop.

If you see:

```text
Failed to load models: Error: 403 "unauthorized"
```

do not reinstall the Power BI plugin first. This is usually a Copilot auth, account, or model-catalog issue, not a Power BI MCP issue.

First check whether the session is otherwise clean:

```text
/mcp
/skills
```

The expected workshop state is:

```text
Power BI Authoring MCP Server (Local) - from powerbi-authoring plugin
powerbi-report-cli
semantic-model-authoring
```

Then refresh the Copilot session:

```text
/user
/logout
/login
/restart
```

If the 403 disappears after restart or re-login, the install was already correct. Treat it as a transient auth/model-catalog failure and continue the lab.
