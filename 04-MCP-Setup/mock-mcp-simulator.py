#!/usr/bin/env python3
"""
Power BI Modeling MCP Server & TMDL Simulator
Used during the Agentic BI workshop to simulate MCP tool calls against a local PBIP project.
"""

import os
import sys
import json
import argparse
from pathlib import Path

def list_tmdl_tables(dataset_dir):
    tables_dir = Path(dataset_dir) / "definition" / "tables"
    if not tables_dir.exists():
        return []
    return [f.stem for f in tables_dir.glob("*.tmdl")]

def get_model_schema(dataset_dir):
    dataset_path = Path(dataset_dir)
    tables_dir = dataset_path / "definition" / "tables"
    schema = {"dataset": dataset_path.name, "tables": {}}

    if tables_dir.exists():
        for tmdl_file in tables_dir.glob("*.tmdl"):
            table_name = tmdl_file.stem
            with open(tmdl_file, "r", encoding="utf-8") as f:
                content = f.read()
            schema["tables"][table_name] = {
                "file": str(tmdl_file),
                "line_count": len(content.splitlines()),
                "has_measures": "measure " in content
            }
    return schema

def add_dax_measure(dataset_dir, table_name, measure_name, dax_expression, format_string="$#,0.00", display_folder=None, description=None):
    tmdl_file = Path(dataset_dir) / "definition" / "tables" / f"{table_name}.tmdl"
    if not tmdl_file.exists():
        return {"status": "error", "message": f"Table file {table_name}.tmdl not found."}

    lines = []
    if description:
        for desc_line in description.splitlines():
            lines.append(f"\t/// {desc_line}")

    # Format multi-line DAX properly
    dax_formatted = dax_expression.strip().replace("\n", "\n\t\t\t")
    lines.append(f"\tmeasure '{measure_name}' = \n\t\t\t{dax_formatted}")
    
    if format_string:
        lines.append(f"\t\tformatString: {format_string}")
    if display_folder:
        lines.append(f"\t\tdisplayFolder: {display_folder}")

    lines.append("") # trailing newline

    new_measure_block = "\n".join(lines)
    
    with open(tmdl_file, "a", encoding="utf-8") as f:
        f.write("\n" + new_measure_block)

    return {
        "status": "success",
        "message": f"Added measure '{measure_name}' to table '{table_name}' in TMDL.",
        "target_file": str(tmdl_file)
    }

def main():
    parser = argparse.ArgumentParser(description="Power BI Modeling MCP Simulator")
    parser.add_argument("--pbip-root", default="c:/Users/aakashkhandelwal/Downloads/Learning/Agentic BI/03-Demo-Project/RetailSales.pbip")
    parser.add_argument("--list-tools", action="store_true")
    parser.add_argument("--get-schema", action="store_true")

    args = parser.parse_args()

    dataset_dir = Path(args.pbip_root).parent / "RetailSales.Dataset"

    if args.list_tools:
        tools = [
            {"name": "get_model_schema", "description": "Inspect TMDL dataset schema"},
            {"name": "add_dax_measure", "description": "Add formatted DAX measure to TMDL file"},
            {"name": "update_tmdl_description", "description": "Auto-document TMDL objects"},
            {"name": "validate_tmdl", "description": "Validate TMDL syntax"},
            {"name": "copy_object", "description": "Copy TMDL measures across datasets"}
        ]
        print(json.dumps(tools, indent=2))
        return

    if args.get_schema:
        print(json.dumps(get_model_schema(dataset_dir), indent=2))
        return

    print("Power BI Modeling MCP Simulator initialized.")
    print(f"Target dataset: {dataset_dir}")
    print(f"Detected TMDL tables: {list_tmdl_tables(dataset_dir)}")

if __name__ == "__main__":
    main()
