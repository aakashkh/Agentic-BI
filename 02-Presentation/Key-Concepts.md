# Key Concepts Deep-Dive: PBIP, Schemas, `.cache`, & Azure DevOps CI/CD

This reference guide provides deep technical specifications on PBIP file structures, JSON schemas, security rules for `.cache`, and enterprise CI/CD integration with Azure DevOps and Microsoft Fabric.

---

## 1. Complete PBIP Folder & File Breakdown

```
RetailSales.pbip                       # [1] Root Pointer File
├── RetailSales.Report/                # [2] Report Folder
│   ├── definition.pbir                # Report pointer schema
│   ├── item.config.json               # Fabric item logical ID
│   └── definition/
│       └── report.json                # Report active theme & pages JSON
├── RetailSales.Dataset/               # [3] Semantic Model Folder
│   ├── definition.pbism               # Dataset pointer schema
│   ├── model.bim                      # TMSL root model JSON
│   ├── item.config.json               # Fabric item logical ID
│   └── definition/                    # TMDL Folder
│       ├── model.tmdl                 # Culture & table refs
│       ├── relationships.tmdl         # Model relationships
│       └── tables/*.tmdl              # Individual TMDL table definitions
└── .cache/ & .pbi/                    # [4] Local Data Cache (DO NOT COMMIT)
    ├── cache.abf                      # Local Analysis Services engine binary data cache
    └── localSettings.json             # Developer local credentials & window state
```

### File Specifications & JSON Schemas

1. **`RetailSales.pbip`**:
   * **Schema**: `https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json`
   * **Version**: `1.0`
   * Specifies relative report folder path and auto-recovery settings.

2. **`definition.pbir` (Report Pointer)**:
   * **Schema**: `https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/1.0.0/schema.json`
   * Links report to dataset via `byPath: { "path": "../RetailSales.Dataset" }`.

3. **`definition.pbism` (Dataset Pointer)**:
   * **Schema**: `https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json`
   * Declares the semantic model boundary.

4. **`item.config.json` (Fabric Identity)**:
   * **Schema**: `https://developer.microsoft.com/json-schemas/fabric/item/config/1.0.0/schema.json`
   * Contains a persistent `logicalId` GUID used by Fabric Git integration to track items across branches.

---

## 2. The `.cache` Aspect & `.gitignore` Rules

When Power BI Desktop opens a `.pbip` project, it initializes a local Analysis Services tabular engine instance and generates:
* **`cache.abf`**: Compressed binary snapshot of all loaded data rows.
* **`localSettings.json`**: Personal developer settings and unencrypted local data source credentials.

### Why `.cache` Must Be Ignored in Git:
1. **Security & Compliance**: Prevents committing confidential production/test data rows to Git repositories.
2. **Repository Hygiene**: Prevents multi-gigabyte binary bloat in Git commit history.
3. **Merge Conflicts**: Prevents constant binary conflicts between developers viewing reports locally.

### Standard `.gitignore`:
```gitignore
.cache/
.pbi/
cache.abf
localSettings.json
*.tmp
```

---

## 3. Azure DevOps CI/CD & Fabric Deployment Pipelines

```
 ┌────────────────────────────────────────────────────────┐
 │ 1. Developer / AI Agent pushes TMDL to Azure Repos     │
 │    `feature/add-time-intelligence`                     │
 └──────────────────────────┬─────────────────────────────┘
                            │ (Pull Request to `main`)
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │ 2. Azure Pipelines (`azure-pipelines.yml`) Runs:       │
 │    • TMDL Syntax Check via @microsoft/powerbi-modeling │
 │    • Best Practice Analyzer (BPA) via Tabular Editor   │
 └──────────────────────────┬─────────────────────────────┘
                            │ (Merged to `main`)
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │ 3. Fabric Git Integration syncs `main` branch directly │
 │    with Development Workspace                          │
 └──────────────────────────┬─────────────────────────────┘
                            │ (Fabric Deployment Pipeline)
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │ 4. Fabric Deployment Pipeline Promotes:                │
 │    Dev Workspace ➔ Test Workspace ➔ Prod Workspace     │
 └────────────────────────────────────────────────────────┘
```

### Sample `azure-pipelines.yml`

```yaml
trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: NodeTool@0
  inputs:
    versionSpec: '18.x'
  displayName: 'Install Node.js'

- script: |
    npx -y @microsoft/powerbi-modeling-mcp --validate ./03-Demo-Project/RetailSales.pbip
  displayName: 'Validate TMDL Syntax via Microsoft MCP'

- script: |
    curl -sSL https://raw.githubusercontent.com/TabularEditor/TabularEditor/master/BPA/BPA-Rules.json -o bpa-rules.json
    echo "Running Tabular Editor BPA check on TMDL definitions..."
  displayName: 'Run Best Practice Analyzer (BPA)'
```
