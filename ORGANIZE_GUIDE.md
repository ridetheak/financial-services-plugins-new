# 🔧 文件归档脚本使用指南

## 📋 概述

本项目提供了三个 Python 脚本，用于将本地新增的分析文件按**五大业务类别**进行智能归档，帮助你快速建立企业级的文档库结构。

## 📁 目录结构

```
├── organize_all.sh              # 一键执行整理的实用脚本
├── run_organize.py             # 主要的整理程序
├── verify_organize.py          # 验证整理结果的脚本
├── organize_v3.py             # 深度整理程序
└── organize_workspace.py       # 原始版本脚本
```

## 🚀 快速开始

### 方法 1: 推荐 - 使用 'organize_all.sh' (最简单)

```bash
# 1. 给脚本执行权限
chmod +x organize_all.sh

# 2. 运行一键整理
./organize_all.sh
```

### 方法 2: 使用 'run_organize.py' (完整功能)

```bash
# 1. 运行归档程序
python3 run_organize.py

# 2. 查看整理报告
cat POST_ORGANIZE_REPORT.md

# 3. 验证归档结果
python3 verify_organize.py
```

### 方法 3: 手动运行 (高级用户)

```bash
# 1. 运行深度整理
python3 organize_v3.py

# 2. 验证结果
python3 verify_organize.py
```

## 📂 五大归档类别

| 类别 | 目标目录 | 包含文件 | 说明 |
|------|----------|----------|------|
| **MCP Analysis** | `docs/analysis/mcp/` | MCP_* 接口文档 | MCP 服务接口调研与映射 |
| **Skills Analysis** | `docs/analysis/skills/` | SKILLS_* 文件 | Skills 反向工程分析 |
| **Architecture** | `docs/analysis/architecture/` | DATA_* & DATAPACK_* | 架构论证与实践分析 |
| **Tools** | `tools/` | create_*.py & organize_*.py | 自动化脚本 |
| **Outputs** | `outputs/` | *.xlsx & *_analysis.md | 脚本生成的财务模型 |
| **Base** | `docs/base/` | README_CN.md & 配置文件 | 基础文档与配置 |

## 📊 执行流程

1. **🔧 初始化**: 脚本自动创建目标目录结构
2. **📁 文件匹配**: 根据文件名模式智能识别文件类别
3. **📡 移动文件**: 将文件移动到对应的目标目录
4. **📋 生成报告**: 创建整理完成的索引报告
5. **🔍 验证结果**: 检查文件是否正确归档

## 📄 输出文件

| 文件 | 说明 |
|------|------|
| `POST_ORGANIZE_REPORT.md` | 整理完成后的目录索引报告 |
| `VERIFY_ORGANIZE_REPORT.md` | 验证归档结果的报告 |

## 📝 下一步操作

### 整理完成后

```bash
# 1. 查看变更
git status

# 2. 暂存所有变更
git add .

# 3. 提交变更
git commit -m "docs: organize local analysis files by category"

# 4. 推送到远程
git push
```

### 如果需要重新整理

```bash
# 1. 重新运行整理
./organize_all.sh

# 2. 验证结果
python3 verify_organize.py
```

## 🔧 脚本特点

- **智能匹配**: 根据文件名模式自动识别文件类别
- **错误处理**: 自动跳过已存在的文件，避免冲突
- **验证机制**: 提供验证报告确保归档正确
- **一键执行**: 'organize_all.sh' 提供最简操作
- **可选性**: 支持手动运行或自动执行

## 🔍 验证机制

`verify_organize.py` 脚本会检查：

1. **目标目录**: 是否都存在
2. **预期文件**: 每个目录是否包含预期的文件
3. **额外文件**: 是否有不属于该目录的文件
4. **未归档文件**: 根目录下是否还有未归档的文件

## 📞 常见问题

### Q: 脚本运行后没有移动任何文件？

A: 可能的原因：
- 文件已经在目标位置
- 文件名未符合模式规则
- 文件已被其他脚本移动

### Q: 如何添加新的文件类别？

A: 修改 `run_organize.py` 中的 `config` 字典，添加新的目录和匹配模式。

### Q: 如何处理冲突的文件？

A: 如果目标目录已存在同名文件，脚本会跳过该文件并提示。

## 🔄 维护建议

- **定期整理**: 每当有新的分析文件产生时运行一次脚本
- **验证流程**: 整理后运行 `verify_organize.py` 确保正确性
- **代码分本**: 定期提交整理后的目录结构

---

*本文档按照中文编导规范编写为你提供最佳学习体验*