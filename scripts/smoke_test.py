#!/usr/bin/env python3
"""lhg-slides 冒烟测试：校验生成的 HTML 是否符合 skill 硬性规则。

用法：
    python3 scripts/smoke_test.py <slides.html> [--manifest references/fixtures/fixture-data-manifest.json]

检查项：
    C1 可编辑架构：HTML 必须含 data-edit-slot（原生可编辑，不是事后补丁）
    C2 美学护栏：全部 hex 色值必须在主题预设色板内（禁自定义 hex）
    C3 数据诚实门：data-source/data-key/data-value 必须与 manifest 逐项对齐
    C4 单文件铁律：不许引用外部 script/link（离线可投屏）
退出码 0=全绿，1=有 FAIL。
"""
import json
import re
import sys
from pathlib import Path

# Phase 2 四套主题预设的全部色值（SKILL.md 原创色板）+ 中性色
PALETTE = {
    "#F7F4EE", "#1C1A17", "#A63D2F",   # 墨白
    "#101B2C", "#EDEFF3", "#5B9BD5",   # 黛蓝
    "#EAF0EC", "#22332B", "#3E7C5B",   # 青瓷
    "#1E1A16", "#F3EDE4", "#D08A3C",   # 赭石
    "#FFFFFF", "#000000",              # 中性
}


def check(html: str, manifest: dict) -> list:
    fails = []
    # C1：原生可编辑架构（按属性匹配，避免文案误判）
    if not re.search(r"data-edit-slot\s*=", html):
        fails.append("C1 缺 data-edit-slot（原生可编辑架构缺失）")
    # C2：美学护栏——禁自定义 hex
    for m in re.finditer(r"#([0-9a-fA-F]{6})\b", html):
        color = "#" + m.group(1).upper()
        if color not in PALETTE:
            fails.append(f"C2 自定义 hex {color}（主题锁死，禁自定义）")
    # C3：数据诚实门——图表数字与 manifest 逐项对齐
    sources = manifest.get("sources", {})
    for m in re.finditer(
        r'data-source="([^"]+)"\s+data-key="([^"]+)"\s+data-value="([^"]+)"', html
    ):
        src, key, val = m.groups()
        expect = sources.get(src, {}).get(key)
        if expect is None:
            fails.append(f"C3 无来源登记：{src} / {key}")
        elif expect != val:
            fails.append(f"C3 数字不一致：{src}/{key} 附件原文 {expect}，PPT 写 {val}")
    # C4：单文件铁律——无外部引用
    for m in re.finditer(r'<(?:script|link)[^>]*(?:src|href)="https?://[^"]+"', html):
        fails.append(f"C4 外部依赖：{m.group(0)[:60]}…")
    return fails


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python3 scripts/smoke_test.py <slides.html> [--manifest <json>]")
        return 2
    html_path = Path(sys.argv[1])
    manifest_path = Path("references/fixtures/fixture-data-manifest.json")
    if "--manifest" in sys.argv:
        manifest_path = Path(sys.argv[sys.argv.index("--manifest") + 1])
    html = html_path.read_text(encoding="utf-8")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    fails = check(html, manifest)
    if fails:
        print("❌ 冒烟测试 FAIL：")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("✅ 冒烟测试全绿")
    return 0


if __name__ == "__main__":
    sys.exit(main())
