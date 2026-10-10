# Git PR Quality Gate & Automated CI Validation

This guide explains how to set up GitHub Pull Requests as the human-in-the-loop quality gate when AI Agents modify TMDL code.

---

## 1. The Pull Request Quality Pipeline

```
┌────────────────────────────────────────────────────────┐
│  AI Agent modifies TMDL code on a feature branch       │
│  `feature/agentic-dax-measures`                        │
└──────────────────────────┬─────────────────────────────┘
                           │ (git push & open PR)
                           ▼
┌────────────────────────────────────────────────────────┐
│  GitHub Actions CI Workflow Runs:                      │
│  1. TMDL Syntax Validator                              │
│  2. Tabular Editor Best Practice Analyzer (BPA)        │
│  3. Automated DAX Formatter                            │
└──────────────────────────┬─────────────────────────────┘
                           │ (Passes CI Checks)
                           ▼
┌────────────────────────────────────────────────────────┐
│  Senior BI Engineer Reviews Git Line Diff & Merges PR  │
└────────────────────────────────────────────────────────┘
```

---

## 2. GitHub Actions CI Workflow Sample (`.github/workflows/tmdl-bpa-check.yml`)

```yaml
name: TMDL Model Quality & BPA Check

on:
  pull_request:
    paths:
      - '**/*.tmdl'
      - '**/*.pbip'

jobs:
  validate-tmdl:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Validate TMDL Syntax
        run: |
          python "04-MCP-Setup/mock-mcp-simulator.py" --get-schema

      - name: Tabular Editor Best Practice Analyzer (BPA)
        run: |
          echo "Running Tabular Editor CLI BPA checks against TMDL..."
          # Insert TabularEditor.exe / pbi-tools CLI command here
```

---

## 3. PR Code Review Checklist for BI Engineers

When reviewing an AI Agent's TMDL pull request:

- [ ] **DAX Safety**: Are division operations wrapped in `DIVIDE()` with a fallback value?
- [ ] **Formatting**: Are measure definitions cleanly indented without redundant VARs?
- [ ] **Documentation**: Are `///` description comments present and written in clear business language?
- [ ] **Display Folders**: Are measures categorized in logical `displayFolder` structures?
- [ ] **Metadata Protection**: Are `lineageTag` UUIDs valid and unique?
