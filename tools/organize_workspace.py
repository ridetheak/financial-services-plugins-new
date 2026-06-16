import os
import shutil
from pathlib import Path

def organize_workspace():
    # 1. Define the target directory structure
    # Five main categories: MCP analysis, Skills analysis, architecture analysis, tool scripts, base translations
    categories = {
        "docs/analysis/mcp": {
            "patterns": ["MCP_*", "ACTUAL_INTERFACES_*"],
            "description": "MCP interface research and API mapping"
        },
        "docs/analysis/skills": {
            "patterns": ["SKILLS_*"],
            "description": "Skills reverse engineering and logic analysis"
        },
        "docs/analysis/architecture": {
            "patterns": ["DATA_*", "DATAPACK_*"],
            "description": "Architecture analysis and data processing practices"
        },
        "tools": {
            "patterns": ["create_*.py", "organize_*.py"],
            "description": "Automation tools and maintenance scripts"
        },
        "outputs": {
            "patterns": ["*.xlsx", "*_analysis.md", "apple_*", "baidu_*"],
            "description": "Script-generated financial models and analysis outputs"
        },
        "docs/base": {
            "patterns": ["README_CN.md", "mcp_config_*.json", "marketplace.json", "LOCAL_FILES_INVENTORY.md"],
            "description": "Base configuration, translations, and index files"
        }
    }

    root = Path.cwd()
    print(f"🚀 Starting deep workspace organization: {root}")
    print("-" * 50)

    moved_count = 0

    # 2. Execute classification logic
    for folder, config in categories.items():
        target_dir = root / folder

        # Ensure the target directory exists
        target_dir.mkdir(parents=True, exist_ok=True)

        for pattern in config["patterns"]:
            # Search for matching files under the root directory
            for file_path in root.glob(pattern):
                # Exclude directories themselves and the script itself (if matched)
                if file_path.is_file() and file_path.name != "organize_workspace.py":
                    dest_path = target_dir / file_path.name

                    try:
                        # If the target already exists, remove it first (overwrite/update)
                        if dest_path.exists():
                            dest_path.unlink()

                        shutil.move(str(file_path), str(dest_path))
                        print(f"✅ [{config['description']}] {file_path.name} -> {folder}/")
                        moved_count += 1
                    except Exception as e:
                        print(f"❌ Move failed {file_path.name}: {e}")

    # 3. Clean up empty directories (optional)
    print("-" * 50)
    if moved_count > 0:
        print(f"✨ Organization complete! Moved {moved_count} files in total.")
        print("💡 Tip: run 'git status' to view the clean directory structure.")
    else:
        print("Stopped: no matching new local files found.")

if __name__ == "__main__":
    organize_workspace()
