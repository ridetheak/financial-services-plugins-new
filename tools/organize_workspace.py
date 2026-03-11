import os
import shutil
from pathlib import Path

def organize_workspace():
    # 1. 定义目标目录结构
    # 按照：MCP分析、Skills分析、架构论证、工具脚本、基础翻译 五大类
    categories = {
        "docs/analysis/mcp": {
            "patterns": ["MCP_*", "ACTUAL_INTERFACES_*"],
            "description": "MCP 接口调研与 API 映射"
        },
        "docs/analysis/skills": {
            "patterns": ["SKILLS_*"],
            "description": "Skills 反向工程与逻辑分析"
        },
        "docs/analysis/architecture": {
            "patterns": ["DATA_*", "DATAPACK_*"],
            "description": "架构论证与数据处理实践"
        },
        "tools": {
            "patterns": ["create_*.py", "organize_*.py"],
            "description": "自动化工具与维护脚本"
        },
        "outputs": {
            "patterns": ["*.xlsx", "*_analysis.md", "apple_*", "baidu_*"],
            "description": "脚本生成的财务模型与分析产出"
        },
        "docs/base": {
            "patterns": ["README_CN.md", "mcp_config_*.json", "marketplace.json", "LOCAL_FILES_INVENTORY.md"],
            "description": "基础配置、翻译与索引文件"
        }
    }

    root = Path.cwd()
    print(f"🚀 开始深度整理工作区: {root}")
    print("-" * 50)

    moved_count = 0

    # 2. 执行分类逻辑
    for folder, config in categories.items():
        target_dir = root / folder
        
        # 确保目标目录存在
        target_dir.mkdir(parents=True, exist_ok=True)
        
        for pattern in config["patterns"]:
            # 在根目录下搜索匹配的文件
            for file_path in root.glob(pattern):
                # 排除目录本身和脚本自身（如果匹配到）
                if file_path.is_file() and file_path.name != "organize_workspace.py":
                    dest_path = target_dir / file_path.name
                    
                    try:
                        # 如果目标已存在，先删除（覆盖更新）
                        if dest_path.exists():
                            dest_path.unlink()
                        
                        shutil.move(str(file_path), str(dest_path))
                        print(f"✅ [{config['description']}] {file_path.name} -> {folder}/")
                        moved_count += 1
                    except Exception as e:
                        print(f"❌ 移动失败 {file_path.name}: {e}")

    # 3. 清理空目录（可选）
    print("-" * 50)
    if moved_count > 0:
        print(f"✨ 整理完成！共移动了 {moved_count} 个文件。")
        print("💡 提示: 运行 'git status' 查看整洁的目录结构。")
    else:
        print("止步：没有发现匹配的本地新增文件。")

if __name__ == "__main__":
    organize_workspace()
