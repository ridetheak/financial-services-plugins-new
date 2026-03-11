import os
import shutil

def organize_files():
    # 定义目录结构
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

    print("🚀 开始整理本地文件...")

    for folder, files in structure.items():
        # 创建目录
        target_dir = os.path.join(base_dir, folder)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"📁 已创建目录: {folder}")

        # 移动文件
        for filename in files:
            source_path = os.path.join(base_dir, filename)
            if os.path.exists(source_path):
                target_path = os.path.join(target_dir, filename)
                try:
                    shutil.move(source_path, target_path)
                    print(f"✅ 已移动: {filename} -> {folder}/")
                except Exception as e:
                    print(f"❌ 移动失败 {filename}: {e}")
            else:
                # 检查是否已经在目标位置（防止重复运行报错）
                if not os.path.exists(os.path.join(target_dir, filename)):
                    pass # 文件不存在且不在目标位置，跳过

    print("\n✨ 整理完成！请运行 'git status' 查看新的目录结构。")

if __name__ == "__main__":
    organize_files()
