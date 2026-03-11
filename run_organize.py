import os
import shutil
from pathlib import Path

def organize_v3():
    config = {
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
    print(f"🛠️  开始深度整理工作区: {root}")
    print("-" * 50)

    stats = {k: 0 for k in config.keys()}

    for target_folder, patterns in config.items():
        target_path = root / target_folder
        
        for pattern in patterns:
            for file_path in root.glob(pattern):
                if target_path in file_path.parents or file_path.name == "run_organize.py":
                    continue
                
                if file_path.is_file():
                    target_path.mkdir(parents=True, exist_ok=True)
                    
                    dest = target_path / file_path.name
                    
                    if dest.exists():
                        print(f"⚠️  跳过已存在文件: {file_path.name}")
                        continue
                        
                    try:
                        shutil.move(str(file_path), str(dest))
                        print(f"✅ [{target_folder}] {file_path.name}")
                        stats[target_folder] += 1
                    except Exception as e:
                        print(f"❌ 移动失败 {file_path.name}: {e}")

    print("\n" + "="*40)
    print("📊 归档任务总结")
    print("="*40)
    total = 0
    for folder, count in stats.items():
        if count > 0:
            print(f"{folder.ljust(25)} : {count} 个文件")
            total += count
    
    if total > 0:
        print(f"\n✨ 成功整理 {total} 个文件！")
        print("👉 建议运行 'git status' 查看变更。")
    else:
        print("📭 未发现需要整理的新文件。")

    # 2. 生成整理后索引报告
    report_path = root / "POST_ORGANIZE_REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# 整理完成后的目录索引报告\n\n")
        f.write(f"**生成时间**: {Path(__file__).stat().st_mtime}\n\n")
        f.write("## 📁 文件归档清单\n\n")
        
        for folder, count in stats.items():
            if count > 0:
                f.write(f"### {folder}\n\n")
                target_path = root / folder
                if target_path.exists():
                    files = list(target_path.glob("*"))
                    for file in files:
                        if file.is_file():
                            f.write(f"- {file.name}\n")
                    f.write("\n")
        
        f.write("## 📋 整理统计\n\n")
        f.write(f"- **总计整理文件**: {total} 个\n")
        f.write(f"- **剩余未整理**: 请运行 'git status' 确认\n\n")
        
        f.write("## 🚀 下一步建议\n\n")
        f.write("- [ ] 运行 'git status' 查看变更\n")
        f.write("- [ ] 运行 'git add .\u0027 暂存\n")
        f.write("- [ ] 运行 'git commit -m \"docs: organize local analysis files by category\"\u0027 提交\n")
        f.write("- [ ] 运行 'git push\u0027 推送\n\n")
        
        f.write("---\n\n")
        f.write("*本报告由 run_organize.py 自动生成*\n")

    print(f"\n📋 已生成整理报告: {report_path}")
    print("\n🎯 归档程序执行完毕！")

if __name__ == "__main__":
    organize_v3()
