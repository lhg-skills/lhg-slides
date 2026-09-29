# lhg-slides · HTML 演示文稿生成

> **一句话**：输入大纲或文档，一键生成带美术护栏、可在浏览器内直接编辑的单文件 HTML 演示文稿。
>
> **一键安装**：`npx skills add lhg-skills/lhg-slides`


带美术护栏、可浏览器内编辑的单文件 HTML 演示文稿 skill：**风格先行挑定再批量生成，原生可编辑不返工，美学护栏是硬约束，图表数字与附件逐项对齐**（lhg-skills 出品；生成工作流借鉴 zarazhangrui/frontend-slides（MIT），可编辑运行时借鉴 archlizheng/frontend-slides-editable（MIT），美学方法论借鉴 op7418/guizang-ppt-skill（AGPL-3.0，仅思路，未用其代码与模板资产））。

**流程**：Phase 0 判模式（NOT for 清单）→ Phase 1 七问澄清 + 数据诚实清单（附件数字逐项登记，无来源不许上图）→ Phase 2 风格先行（3 张视觉缩略图看图挑，4 套主题锁死禁自定义 hex，定稿才批量）→ Phase 3 生成（零依赖单文件、16:9 固定舞台、槽位/对象双模式第一页植入、编辑运行时随文件交付）→ Phase 4 美学护栏（主题锁死/字号收敛/hero-non-hero 交替/动效克制四条硬约束）→ Phase 5 中文排版专项（字体栈/标点/标题降档）→ Phase 6 数据诚实门（生成后逐项核对，拦截返工）→ Phase 7 双模式交付（只读轻量版 vs 可编辑版）+ 演讲者模式。

**触发**：用户说"做个 PPT / 演示文稿 / 把材料做成幻灯片 / HTML-PPT"时使用。

## 安装

一键安装：`npx skills add lhg-skills/lhg-slides`

- 通用：将本仓库放到各平台的 skill 目录（如 `~/.agents/skills/lhg-slides/`，注意 SKILL.md 须在目录根）。
- Coze：在扣子编程（code.coze.cn）→ 导入项目 → 本地上传本仓库 zip 包，平台会识别为 skill 类型。
- Trae：设置 → 技能 → 上传技能，选择本仓库 zip 包（或把目录放到 `~/.trae-cn/skills/`，国区版注意路径）。
- 平台无关：本 skill 写法平台中立（联网搜索/抓取全文/只读子 agent/任务清单/文件搜索/编辑），不依赖任何单一生态的专有工具名。

## 自检与反馈

本 skill 每次执行后自动做一次轻量自检（对照美学护栏四条 + 数据诚实门四项）；只有发现疑似自身缺陷时，才运行 `references/smoke-test.md` 标准用例并输出质检报告。报告经你确认后，可一键向 GitHub 提交 `[QC]` issue（模板见 `.github/ISSUE_TEMPLATE/qc-report.md`）。

## 版本

- 1.0.0（2026-09-29）：首版。三合一再创造：生成工作流（zarazhangrui/frontend-slides，MIT）+ 原生可编辑架构（archlizheng/frontend-slides-editable，MIT）+ 美学方法论（op7418/guizang-ppt-skill，AGPL-3.0，仅思路借鉴，未使用其代码与模板资产）；升级点：原生可编辑、风格先行、美学护栏硬约束、数据诚实门、中文排版专项、双模式交付、演讲者模式。

## 什么时候用 / 什么时候不用

**用它，当你**：
- 要做分享/路演，需要快速出一版能看的演示文稿
- 想要可二次编辑的 HTML slides，而不是导出的图片式 PPT
- 在意中文排版和视觉质感

**别用它，当你**：
- 必须交付 PowerPoint .pptx 原生文件
- 印刷级、像素级排版需求

---

## English

**lhg-slides — Single-file HTML slides.** Turn an outline or document into a polished, browser-editable HTML presentation in one file — with art-direction guardrails so the result doesn't look AI-generated. Install: `npx skills add lhg-skills/lhg-slides`.

---

## FAQ

**Q：lhg-slides 有什么用？**
适合的场景：有大纲或文档，想一键生成能在浏览器里直接编辑的单文件 HTML 演示文稿，还带美术护栏不做成 AI 味。

**Q：免费吗？怎么安装？**
开源免费（MIT，可商用、保留署名）。安装：`npx skills add lhg-skills/lhg-slides`，或 clone 仓库把 `SKILL.md` 放进对应平台的 skills 目录。

**Q：支持哪些 AI 平台？**
平台中立纯 Markdown 流程描述，Claude Code、Codex、豆包智能体、Workbuddy、扣子、Trae 等支持 Markdown 指令的环境都可用。更多 skill 见 [lhg-skills 组织主页](https://github.com/lhg-skills)。

---

## lhg-skills 矩阵

刘洪光出品的中文 Agent Skills，全开源：

| Skill | 名称 | 一句话 |
|---|---|---|
| `lhg-writing` | 中文写作 | 风格指纹 → Orwell 六规则 → AI 味诊断，写出有人味的中文 |
| `lhg-slides` | HTML 演示文稿 | 大纲/文档一键生成可编辑的单文件 HTML slides |
| `lhg-trend` | 近30天热点扫描 | 话题火不火、为什么火、还能不能追 |
| `lhg-deep-research` | 深度调研 | 多源检索 → 结构化中文调研报告 |
| `lhg-benchmark-topic-factory` | 对标拆解选题工厂 | 找对标 → 逆向 100 条选题库 → 口播文案 |
| `lhg-net` | 互联网能力层 | 中文优先多平台取数，取不到诚实说 |
| `lhg-craft` | AI 编程工程规范 | 分级澄清 → TDD → 独立评审 → 证据门禁 |
| `lhg-debug` | 系统化调试 | 复现 → 定位 → 修复 → 验证 |
| `lhg-secure` | 代码安全审计 | 九维度扫描 + 对抗验证，分级风险清单 |
| `lhg-finder` | 找 skill 质检门 | 装第三方 skill 前的 blocker 检查 + 六维评分 |

安装任意一个：`npx skills add lhg-skills/<上表 slug>`

---

## 出品：刘洪光

本 skill 由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 视频号：搜「刘洪光实名上网」
- 微信：lhgsmsw
