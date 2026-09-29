# lhg-slides · HTML 演示文稿生成

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

## 出品：刘洪光

本 skill 由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 视频号：搜「刘洪光实名上网」
- 微信：lhgsmsw
