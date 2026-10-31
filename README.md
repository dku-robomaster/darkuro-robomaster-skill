# DKU RoboMaster 战队 Skill

给昆山杜克大学 RoboMaster 队员使用的共享工作入口。AI 按需读取战队背景与工程方法，通过目录定位原始 PDF，再直接打开原件回答规则、机械、电控、视觉、裁判系统、采购和培训问题。

资料正文以原始 PDF 随包提供。保留 Skill 必需的 Markdown 指引和 JSON 文件目录，不打包 PDF 提取全文或 Wiki 文字快照。

## 随包内容

| 内容 | 数量 / 路径 |
| --- | --- |
| Skill 入口 | `skills/dku-robomaster/SKILL.md` |
| 规则、手册、制作规范和协议原始 PDF | 19 份；Skill 内的 `assets/rules-originals/` |
| 战队岗位说明原始 PDF | 1 份；`assets/division-roles-original.pdf` |
| 路径、来源、大小与 SHA-256 | `references/bundled-library.json` |
| 稳定背景与工程方法 | `references/` 内的 Markdown 指引 |
| PDF 文件目录工具 | `scripts/pdf_catalog.py` |

文件目录只按名称与元数据定位文件，不检索 PDF 正文。AI 使用其 PDF 阅读工具打开原件并查看章节、表格、图片和附注；阅读工具的能力由所使用的客户端提供。

本版整理于 **2026-11-01**，原始资料副本采集记录为 **2026-10-30**，约 97 MiB。同时保留 2026 和 2027 文件。某份 2027 RMUC 英文手册位于原有 `2026/` 子目录，适用年份必须按文件名和原文确认。打包日期不等于官方实时核验日期。

## 安装

需要 **Python 3.9 或更新版本**。安装器和目录工具只使用标准库。

在仓库根目录运行：

```bash
# Codex 本地用户级安装
python3 install.py --app codex

# Claude Code 本地用户级安装
python3 install.py --app claude
```

macOS 可双击 `Install.command`，Windows 可双击 `Install.bat`，默认安装到 Codex。

Codex 安装位置为 `~/.agents/skills/dku-robomaster`，Claude Code 为 `~/.claude/skills/dku-robomaster`。支持 `AGENTS.md` 的助手也可直接打开本仓库，按根目录指引使用随包 Skill。以上是本地安装，不会保存到 ChatGPT 网页账户。

更新本地安装：

```bash
git pull
python3 install.py --app codex --replace
```

`--replace` 会先校验并完整复制新版本，再将旧副本备份到该应用用户目录的 `skill-backups/`。旧版文字快照只会留在旧副本备份中，不进入新安装。首次安装遇到同名目录会停止。

其他工具可以复制整个 `skills/dku-robomaster` 文件夹到它们支持的 Skill 目录，或指定目录：

```bash
python3 install.py --destination /path/to/project/.agents/skills
```

安装后新建会话或刷新 Skill 列表，并调用 `dku-robomaster`。

## 使用原始 PDF

可以对助手说：

> 使用 dku-robomaster。我们准备参加 RMUL 3V3，请从原始 PDF 核对步兵的相关要求，注明文件版本、章节和页码，并检查官网有无更新。

直接查看 PDF 目录：

```bash
python3 skills/dku-robomaster/scripts/pdf_catalog.py list
python3 skills/dku-robomaster/scripts/pdf_catalog.py find 2027 规范
```

结果中的 `pdf_path` 是可供 PDF 工具打开的完整路径，`relative_path` 是 Skill 内的相对路径。目录不读取或输出资料正文。

官方 Wiki、论坛和 [战队资料站](https://rm.mimihuka.space/) 通过链接访问。讲座、CAD、视频、采购及动态队内记录由成员按需提供。

## 上传 GitHub

仓库地址为 https://github.com/mimihuka/darkuro-robomaster-skill 。

维护者在本目录上传：

```bash
git push -u origin main
```

若在新的本地副本尚未设置远程地址：

```bash
git remote add origin https://github.com/mimihuka/darkuro-robomaster-skill.git
```

上传完成后，队员可克隆仓库并运行上述安装器。本 Skill 不同步某位队员的聊天历史、账号权限或未记录的队内决策。

## 维护与检查

```bash
python3 tools/verify_bundle.py
```

校验包括所有 20 份 PDF 的文件头、大小和 SHA-256，以及目录、Skill 引用与脚本语法；同时检查未混入文字快照。

新增规则版本时保留官方原件和原文件名，在 `references/bundled-library.json` 中登记来源路径、大小和哈希，再更新目录与日期。文件名、年份或目录只帮助定位；回答现行规则前，仍需核对 [官方公告](https://www.robomaster.com/zh-CN/resource/announcement/competition)、[规则 / 资料中心](https://bbs.robomaster.com/wiki/20204847/811012?source=7) 和最新勘误。

本地 Skill 目录依据：[Codex](https://learn.chatgpt.com/docs/build-skills)、[Claude Code](https://code.claude.com/docs/en/skills)。第三方文件权利及授权范围见 [NOTICE.md](NOTICE.md)。
