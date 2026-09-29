# 标准冒烟测试（skill 自检用）

> 触发时机：SKILL.md「自检与反馈」命中疑似自身缺陷时运行。
> 说明：`scripts/smoke_test.py` 校验生成的 HTML 是否符合本 skill 硬性规则
> （C1 原生可编辑架构 / C2 美学护栏禁自定义 hex / C3 数据诚实门 / C4 单文件铁律）；
> 数据诚实门用 `references/fixtures/fixture-data-manifest.json` 模拟"附件原文"。
> 以下全部用例已于 2026-09-29 实测通过。

## S-1 合规 HTML 全绿

- fixture：`references/fixtures/fixture-slides-good.html`（含 data-edit-slot、仅用主题色板色值、图表数字与 manifest 一致、无外部引用）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-slides-good.html
  ```
  → 退出码 0，`✅ 冒烟测试全绿`

## S-2 缺 data-edit-slot

- fixture：`references/fixtures/fixture-slides-no-slot.html`（无 data-edit-slot 属性）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-slides-no-slot.html
  ```
  → 退出码 1，FAIL 含 `C1 缺 data-edit-slot`

## S-3 自定义 hex 被拦截

- fixture：`references/fixtures/fixture-slides-custom-hex.html`（含色板外的 `#BADA55`）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-slides-custom-hex.html
  ```
  → 退出码 1，FAIL 含 `C2 自定义 hex #BADA55`

## S-4 图表数字与附件不一致被拦截

- fixture：`references/fixtures/fixture-slides-data-mismatch.html`（data-value 13.0 vs manifest 12.6）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-slides-data-mismatch.html --manifest references/fixtures/fixture-data-manifest.json
  ```
  → 退出码 1，FAIL 含 `C3 数字不一致`

## S-5 外部依赖被拦截

- fixture：`references/fixtures/fixture-slides-external-dep.html`（引用外部图表库 CDN）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-slides-external-dep.html
  ```
  → 退出码 1，FAIL 含 `C4 外部依赖`

## S-6 人工检查项（脚本扫不到的）

- [ ] hero/non-hero 交替节奏：连续两页 hero 或连续三页纯文字页即节奏事故
- [ ] 中文字号收敛：是否只用了 44/32/18/13 四档
- [ ] 动效克制：是否只有淡入/位移两种、时长 ≤ 400ms
- [ ] 中文排版：全角标点、中英混排空格、标题 ≤ 12 字
- [ ] 演讲者模式：备注/计时/激光笔是否可用
