import os
from pathlib import Path

def verify_organize():
    # 1. 定义预期的目录结构
    expected_structure = {
        "docs/analysis/mcp": [
            "MCP_*", "ACTUAL_INTERFACES_*", "mcp_config_*.json"
        ],
        "docs/analysis/skills": [
            "SKILLS_*", "**/SKILL_CN.md"
        ],
        "docs/analysis/architecture": [
            "DATA_*", "DATAPACK_*"
        ],
        "tools": [
            "create_*.py", "organize_*.py"
        ],
        "outputs": [
            "*.xlsx", "*_analysis.md", "apple_*", "baidu_*", "alibaba_*"
        ],
        "docs/base": [
            "README_CN.md", "marketplace.json", "package*.json", "LOCAL_FILES_INVENTORY.md"
        ]
    }

    root = Path.cwd()
    print(f"🔍 开始验证文件归档情况...")
    print(f"📁 根目录: {root}")
    print("-" * 50)

    # 2. 检查每个目录
    missing_files = []
    extra_files = []
    
    for target_folder, patterns in expected_structure.items():
        target_path = root / target_folder
        
        if not target_path.exists():
            print(f"❌ 目录不存在: {target_folder}")
            continue
        
        # 检查该目录下是否包含预期的文件
        found_any = False
        for pattern in patterns:
            for file_path in target_path.glob(pattern):
                if file_path.is_file():
                    found_any = True
                    break
        
        if not found_any:
            missing_files.append(target_folder)
        
        # 检查是否有额外的文件
        for file_path in target_path.glob("*"):
            if file_path.is_file():
                matched = False
                for pattern in patterns:
                    if file_path.match(pattern):
                        matched = True
                        break
                if not matched:
                    extra_files.append((target_folder, file_path.name))

    # 3. 检查根目录下是否还有未归档的文件
    root_files = []
    for file_path in root.glob("*"):
        if file_path.is_file() and file_path.name not in ["organize_all.sh", "run_organize.py", "verify_organize.py", "POST_ORGANIZE_REPORT.md"]:
            root_files.append(file_path.name)

    # 4. 生成验证报告
    report_path = root / "VERIFY_ORGANIZE_REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# 🔍 文件归档验证报告\n\n")
        f.write(f"**验证时间**: {Path(__file__).stat().st_mtime}\n\n")
        
        # 验证结果
        f.write("## ✅ 验证结果\n\n")
        
        if not missing_files and not extra_files and not root_files:
            f.write("- **✅ 所有文件都已正确归档！**\n")
        else:
            if missing_files:
                f.write("- **❌ 以下目录缺少预期文件:**\n")
                for folder in missing_files:
                    f.write(f"  - {folder}\n")
            
            if extra_files:
                f.write("- **⚠️  以下目录包含额外文件:**\n")
                for folder, filename in extra_files:
                    f.write(f"  - {folder}/{filename}\n")
            
            if root_files:
                f.write("- **⚠️  以下文件仍在根目录未归档:**\n")
                for filename in root_files:
                    f.write(f"  - {filename}\n")
        
        # 建议
        f.write("\n## 💡 建议\n\n")
        if not missing_files and not extra_files and not root_files:
            f.write("- **✅ 无需操作，归档已完成！**\n")
        else:
            f.write("- 运行 'git status' 查看具体变更\n")
            f.write("- 手动检查缺失的文件\n")
            f.write("- 运行 'python3 run_organize.py' 重新整理\n")
        
        f.write("\n---\n\n")
        f.write("*本报告由 verify_organize.py 自动生成*\n")

    # 5. 控制台输出结果
    print(f"\n📋 验证报告已生成: {report_path}")
    
    if not missing_files and not extra_files and not root_files:
        print("✅ ✅ ✅ 验证通过！所有文件都已正确归档！")
        print("💡 建议: 现在可以提交这些变更了。")
    else:
        print("⚠️  ⚠️  ⚠️ 验证发现问题：")
        if missing_files:
            print(f"❌ 缺失文件: {len(missing_files)} 个目录")
        if extra_files:
            print(f"⚠️ 额外文件: {len(extra_files)} 个")
        if root_files:
            print(f"⚠️ 未归档文件: {len(root_files)} 个")
        
        print(f"\n💡 建议: 运行 'python3 run_organize.py' 重新整理")

if __name__ == "__main__":
    verify_organize()
