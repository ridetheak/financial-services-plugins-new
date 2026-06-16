import os
import shutil
from pathlib import Path

def organize_v3():
    # 1. Configure classification rules (target directory: match patterns)
    config = {
        "docs/analysis/mcp": [
            "MCP_*", "ACTUAL_INTERFACES_*", "mcp_config_*.json"
        ],
        "docs/analysis/skills": [
            "SKILLS_*", "**/SKILL_CN.md"  # includes translations in subdirectories
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
    print(f"🛠️  Initializing archive program...")
    print(f"📂 Root directory: {root}\n")

    stats = {k: 0 for k in config.keys()}

    # 2. Execute archiving
    for target_folder, patterns in config.items():
        target_path = root / target_folder

        for pattern in patterns:
            # Use rglob to support recursive search (handles files in subdirectories)
            for file_path in root.glob(pattern):
                # Exclude files already in the target directory, exclude the script itself
                if target_path in file_path.parents or file_path.name == "organize_v3.py":
                    continue

                if file_path.is_file():
                    # Ensure the target directory exists
                    target_path.mkdir(parents=True, exist_ok=True)

                    dest = target_path / file_path.name

                    # Handle filename conflicts
                    if dest.exists():
                        print(f"⚠️  Skipping already-existing file: {file_path.name}")
                        continue

                    try:
                        shutil.move(str(file_path), str(dest))
                        print(f"✅ [{target_folder}] {file_path.name}")
                        stats[target_folder] += 1
                    except Exception as e:
                        print(f"❌ Move failed {file_path.name}: {e}")

    # 3. Generate organization report
    print("\n" + "="*40)
    print("📊 Archive task summary")
    print("="*40)
    total = 0
    for folder, count in stats.items():
        if count > 0:
            print(f"{folder.ljust(25)} : {count} files")
            total += count

    if total > 0:
        print(f"\n✨ Successfully organized {total} files!")
        print("👉 Recommended: run 'git status' to confirm changes.")
    else:
        print("📭 No new files found that need organizing.")

if __name__ == "__main__":
    organize_v3()
