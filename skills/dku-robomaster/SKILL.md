---
name: dku-robomaster
description: 为 DKU RoboMaster 战队处理规则核对、机械、电控、视觉、裁判系统、采购、培训和项目规划问题。随包资料为原始 PDF，通过文件目录定位后直接阅读原件。Use for DKU RoboMaster onboarding, RMUL/RMUC rules, engineering and team knowledge retrieval from original PDFs.
---

# DKU RoboMaster 战队助手

先读 [战队背景](references/team-context.md)、[资料来源](references/knowledge-sources.md) 和 [PDF 目录](references/bundled-library.md)。技术任务再读 [工程流程](references/engineering-workflows.md)，分工任务读 [组别职责](references/division-roles.md)。所有相对路径以本 Skill 目录为基准。

## 从原始 PDF 回答

1. 先确定赛季、赛项（RMUL 3V3、RMUL 步兵对抗赛、RMUC 等）、机器人类型和适用版本。
2. 用 `python3 scripts/pdf_catalog.py find 2027 规范` 或 `list` 定位原始 PDF。该脚本只按文件名和目录元数据筛选，不检索 PDF 正文。
3. 使用可用的 PDF 阅读工具直接打开返回的原件路径，查看相关章节、表格、图片及附注。可以按需临时解析 PDF，但不要把派生全文或文字快照存入此包。
4. 回答规则问题时注明文件名、版本、章节或页码，并区分强制要求、官方建议、团队决策和工程建议。工具打不开 PDF 或相关页时明确说明缺少原文证据。
5. 对现行限制、资格、期限、价格、协议及采购，另外核对官方最新文件和勘误，注明实际核对日期。文件打包日期不能证明官方内容未变。
6. 不仅凭摘要、文件名、CAD 元数据或视频元数据作出结构或合规判断。

## 随包资料与外部来源

- `assets/rules-originals/` 保留 19 份规则、手册和协议原始 PDF；`assets/division-roles-original.pdf` 是岗位说明原件。
- `references/bundled-library.json` 仅记录文件路径、来源路径、字节数和 SHA-256。按 [PDF 目录](references/bundled-library.md) 选择文件；以文件名和原文确认赛季，不能仅凭父目录推断。
- 官方 Wiki、论坛和资料站通过 [资料来源](references/knowledge-sources.md) 中的链接访问。讲座、CAD、采购记录及项目状态按任务从队内资料库获取。
- 保留 Skill 必需的 Markdown 指引与 JSON 目录；资料正文以原始 PDF 随包提供。

## 团队知识

用稳定背景帮助新人理解术语与下一步。库存、报名、赞助、预算和进度须由最新队内记录确认；招新示例中的 Jetson、YOLO 或相机不构成采购记录。没有依据的决策明确说未知。未经授权，不把私人对话、账号凭据或提案写成团队共享事实。

本版整理于 2026-11-01。官方发布新版本后，添加原件并更新目录、校验值与版本说明。
