# Retail Sales Demo Project (`RetailSales.pbip`)

Welcome to the live demo project for the **Agentic Business Intelligence** workshop!

This project is formatted in **Power BI Project (`.pbip`)** format using **TMDL (Tabular Model Definition Language)**, providing a fully decomposed, plain-text semantic model and modern PBIR report definition.

---

## 📁 Project Structure

```
03-Demo-Project/
├── RetailSales.pbip              # Root pointer file (open with Power BI Desktop)
├── generate_data.py               # Standalone Python script to regenerate synthetic CSV data
├── Data/                          # CSV data files (5,000 transactions, 2023–2026)
│   ├── FactSales.csv              # Transactional sales rows
│   ├── DimCustomer.csv            # Customer demographics & segments
│   ├── DimProduct.csv             # Product catalog & categories
│   └── DimDate.csv                # Complete calendar dimension (2023–2026)
├── RetailSales.Report/            # Report visual definition folder (PBIR)
│   ├── definition.pbir            # Report-to-dataset pointer schema
│   ├── item.config.json           # Fabric logicalId identifier
│   └── definition/report.json     # Visual layouts & theme definitions
└── RetailSales.Dataset/           # Semantic model folder (TMDL)
    ├── definition.pbism           # Dataset boundary schema
    ├── model.bim                  # TMSL root model definition
    └── definition/
        ├── model.tmdl             # Model properties & culture info
        ├── relationships.tmdl     # Star schema relationship definitions
        └── tables/                # Modular TMDL table files
            ├── FactSales.tmdl     # Sales transactions & M partition
            ├── DimCustomer.tmdl   # Customer dimension & M partition
            ├── DimProduct.tmdl    # Product dimension & M partition
            ├── DimDate.tmdl       # Date dimension (dataCategory: Time)
            └── SalesMetrics.tmdl  # Disconnected DAX measure container
```

---

## 🚀 How to Run & Use This Demo Project

### Option A: Open in Power BI Desktop (Visual Experience)
1. Ensure you have **Power BI Desktop (August 2026 release or later)** installed.
2. Double-click [`RetailSales.pbip`](RetailSales.pbip).
3. Click **Home ➔ Refresh** to load data from the local CSV files in the `Data/` folder.
4. Switch to **Model View** to inspect the star schema relationships and measures.

### Option B: Open in VS Code (Code-First & Agentic Modeling)
1. Open the repository root or this folder in **VS Code**.
2. Navigate to `RetailSales.Dataset/definition/tables/`.
3. Open any `.tmdl` file (e.g. `SalesMetrics.tmdl` or `FactSales.tmdl`) to inspect measures, columns, and M queries directly in plain text.
4. Connect the **Power BI Modeling MCP Server** to programmatically add measures or update documentation.

### Option C: Regenerate Synthetic Data
If you wish to refresh or expand the synthetic retail dataset:
```powershell
python generate_data.py
```
This regenerates the 4 CSV files in `Data/` with fresh random transactions while preserving schema contracts.

---

## 🔗 Related Documentation
* 📖 **PBIX to PBIP Rosetta Stone**: [`../02-Presentation/PBIX-to-PBIP-Mapping-Guide.md`](../02-Presentation/PBIX-to-PBIP-Mapping-Guide.md)
* 🔌 **MCP Setup Guide**: [`../04-MCP-Setup/mcp-config-guide.md`](../04-MCP-Setup/mcp-config-guide.md)
* ⚡ **Prompting Playbook**: [`../05-Prompts-and-Workflows/MCP-Prompting-Best-Practices.md`](../05-Prompts-and-Workflows/MCP-Prompting-Best-Practices.md)
