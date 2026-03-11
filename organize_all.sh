#!/bin/bash

echo "🚀 开始整理本地文件..."
echo "==========================="

# 1. 运行 Python 归档脚本
python3 run_organize.py

# 2. 显示整理后的目录结构
echo "\n📁 整理完成后的目录结构:"
echo "==========================="
tree -L 3 -I '__pycache__' 2>/dev/null || find . -type d | head -20

# 3. 显示整理报告
echo "\n📋 整理报告内容:"
echo "==========================="
if [ -f "POST_ORGANIZE_REPORT.md" ]; then
    head -20 POST_ORGANIZE_REPORT.md
    echo "... (更多内容请查看 POST_ORGANIZE_REPORT.md)"
else
    echo "❌ 报告文件未生成，请检查脚本执行情况。"
fi

echo "\n🎯 整理完成！"
echo "==========================="
echo "\n💡 建议下一步操作:"
echo "  1. 运行 'git status' 查看变更"
echo "  2. 运行 'git add .' 暂存"
echo "  3. 运行 'git commit -m \"docs: organize local analysis files by category\"' 提交"
echo "  4. 运行 'git push' 推送"
echo ""
echo "📝 整理报告已保存到: POST_ORGANIZE_REPORT.md"
echo ""
echo "🔧 如需重新整理，请运行: python3 run_organize.py"
echo ""
