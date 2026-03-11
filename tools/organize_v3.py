import os
import shutil
from pathlib import Path

def organize_v3():
    # 1. 配置分类规则 (目标目录: 匹配模式)
    config = {
        "docs/analysis/mcp": [
            "MCP_*", "ACTUAL_INTERFACES_*", "mcp_config_*.json"
        ],
        "docs/analysis/skills": [
            "SKILLS_*", "**/SKILL_CN.md"  # 包含子目录中的翻译
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
    print(f"🛠️  正在初始化归档程序...")
    print(f"📂 根目录: {root}\n")

    stats = {k: 0 for k in config.keys()}
    
    # 2. 执行归档
    for target_folder, patterns in config.items():
        target_path = root / target_folder
        
        for pattern in patterns:
            # 使用 rglob 支持递归搜索（处理子目录中的文件）
            for file_path in root.glob(pattern):
                # 排除已经在目标目录中的文件，排除脚本自身
                if target_path in file_path.parents or file_path.name == "organize_v3.py":
                    continue
                
                if file_path.is_file():
                    # 确保目标目录存在
                    target_path.mkdir(parents=True, exist_ok=True)
                    
                    dest = target_path / file_path.name
                    
                    # 处理重名冲突
                    if dest.exists():
                        print(f"⚠️  跳过已存在文件: {file_path.name}")
                        continue
                        
                    try:
                        shutil.move(str(file_path), str(dest))
                        print(f"✅ [{target_folder}] {file_path.name}")
                        stats[target_folder] += 1
                    except Exception as e:
                        print(f"❌ 移动失败 {file_path.name}: {e}")

    # 3. 生成整理报告
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
        print("👉 建议运行 'git status' 确认变更。")
    else:
        print("📭 未发现需要整理的新文件。")

if __name__ == "__main__":
    organize_v3()
