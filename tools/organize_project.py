import os
import shutil

def organize_files():
    # Define the directory structure
    base_dir = os.getcwd()
    structure = {
        "docs/analysis/mcp": [
            "ACTUAL_INTERFACES_INFERRED_CN.md",
            "MCP_AKSHARE_QUICK_REFERENCE_CN.md",
            "MCP_ANALYSIS_SUMMARY.md",
            "MCP_APIS_DISCOVERY_CN.md",
            "MCP_DISCOVERY_GUIDE_CN.md",
            "MCP_DOCUMENTATION_INDEX_CN.md",
            "MCP_INTERFACES_COMPLETE_SUMMARY_CN.md",
            "MCP_INTERFACES_COMPREHENSIVE_ANSWER_CN.md",
            "MCP_INTERFACES_FINAL_SUMMARY_CN.md",
            "MCP_INTERFACES_PARAMETERS_SUMMARY.md",
            "MCP_INTERFACE_CATALOG_CN.md",
            "MCP_QUICK_FACTS_CN.md",
            "MCP_SERVICES_AKSHARE_MAPPING_CN.md",
            "MCP_SERVICES_ANALYSIS_CN.md"
        ],
        "docs/analysis/skills": [
            "SKILLS_ANALYSIS_README.md",
            "SKILLS_INFERENCE_ANALYSIS_SUMMARY.md",
            "SKILLS_INFERENCE_QUICK_GUIDE.md",
            "SKILLS_TO_APIS_MAPPING_CN.md"
        ],
        "docs/analysis/architecture": [
            "DATAPACK_BUILDER_IMPROVEMENTS_QUICK_REFERENCE_CN.md",
            "DATAPACK_BUILDER_PRACTICE_ANALYSIS_CN.md",
            "DATA_HANDLING_COMPARISON_TABLE_CN.md",
            "DATA_PROCESSING_ARCHITECTURE_ANALYSIS_CN.md"
        ],
        "tools": [
            "create_apple_model.py",
            "create_apple_model_complete.py",
            "create_baidu_comps.py",
            "create_baidu_dcf.py"
        ],
        "outputs": [
            "apple_3_statement_model.xlsx",
            "baidu_comparable_analysis.xlsx",
            "alibaba_competitive_analysis.md"
        ],
        "docs/base": [
            "README_CN.md",
            "mcp_config_template.json",
            "marketplace.json",
            "LOCAL_FILES_INVENTORY.md"
        ]
    }

    print("🚀 Starting local file organization...")

    for folder, files in structure.items():
        # Create directory
        target_dir = os.path.join(base_dir, folder)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"📁 Created directory: {folder}")

        # Move files
        for filename in files:
            source_path = os.path.join(base_dir, filename)
            if os.path.exists(source_path):
                target_path = os.path.join(target_dir, filename)
                try:
                    shutil.move(source_path, target_path)
                    print(f"✅ Moved: {filename} -> {folder}/")
                except Exception as e:
                    print(f"❌ Move failed {filename}: {e}")
            else:
                # Check if the file is already at the target location (prevents errors on re-run)
                if not os.path.exists(os.path.join(target_dir, filename)):
                    pass # File does not exist and is not at the target location, skip

    print("\n✨ Organization complete! Run 'git status' to review the new directory structure.")

if __name__ == "__main__":
    organize_files()
