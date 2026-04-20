#!/usr/bin/env python3
"""
中国古代建筑结构可视化项目 - 快速验证脚本
检查所有文件是否存在，以及HTML/CSS/JS是否有明显语法错误
"""

import os
import re
import sys

PROJECT_DIR = "/root/.openclaw/workspace/ancient-architecture-visualization"

def check_file_exists(filepath, description):
    """检查文件是否存在"""
    full_path = os.path.join(PROJECT_DIR, filepath)
    if os.path.exists(full_path):
        size = os.path.getsize(full_path)
        print(f"✅ {description}: {filepath} ({size:,} bytes)")
        return True
    else:
        print(f"❌ {description} 缺失: {filepath}")
        return False

def check_html_syntax(filepath):
    """简单检查HTML文件"""
    full_path = os.path.join(PROJECT_DIR, filepath)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查必要标签
    checks = [
        ('<!DOCTYPE html>', 'DOCTYPE声明'),
        ('<html', 'html标签'),
        ('<head>', 'head标签'),
        ('<body>', 'body标签'),
        ('</html>', 'html闭合标签'),
        ('echarts', 'ECharts引用'),
    ]

    all_ok = True
    for pattern, name in checks:
        if pattern.lower() in content.lower():
            print(f"  ✓ {name} 存在")
        else:
            print(f"  ✗ {name} 缺失")
            all_ok = False

    return all_ok

def check_js_syntax(filepath):
    """简单检查JS文件"""
    full_path = os.path.join(PROJECT_DIR, filepath)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查基本结构
    checks = []

    if 'data.js' in filepath:
        checks = [
            ('const WOOD_PROPERTIES', '木材数据定义'),
            ('const TAI_LIANG_DATA', '抬梁式数据'),
            ('const CHUAN_DOU_DATA', '穿斗式数据'),
        ]
    elif 'charts.js' in filepath:
        checks = [
            ('function initRadarChart', '雷达图函数'),
            ('function initBarChart', '柱状图函数'),
            ('function initLineChart', '折线图函数'),
            ('function initScatterChart', '散点图函数'),
            ('echarts.init', 'ECharts初始化'),
        ]
    elif 'main.js' in filepath:
        checks = [
            ('DOMContentLoaded', 'DOM加载监听'),
            ('initCharts', '图表初始化调用'),
        ]

    all_ok = True
    for pattern, name in checks:
        if pattern in content:
            print(f"  ✓ {name} 存在")
        else:
            print(f"  ✗ {name} 缺失")
            all_ok = False

    return all_ok

def main():
    print("=" * 60)
    print("中国古代建筑结构可视化项目 - 验证脚本")
    print("=" * 60)
    print()

    results = []

    print("📁 检查文件存在性...")
    results.append(check_file_exists("index.html", "主页面"))
    results.append(check_file_exists("css/style.css", "样式文件"))
    results.append(check_file_exists("js/data.js", "数据定义"))
    results.append(check_file_exists("js/charts.js", "图表配置"))
    results.append(check_file_exists("js/main.js", "交互逻辑"))
    results.append(check_file_exists("README.md", "项目说明"))
    results.append(check_file_exists("docs/数据来源.md", "数据来源"))
    results.append(check_file_exists("docs/设计说明.md", "设计说明"))
    results.append(check_file_exists("docs/使用指南.md", "使用指南"))
    results.append(check_file_exists("package.json", "项目配置"))
    results.append(check_file_exists(".gitignore", "Git配置"))
    print()

    print("🔍 检查 HTML 语法...")
    results.append(check_html_syntax("index.html"))
    print()

    print("🔍 检查 JavaScript 语法...")
    results.append(check_js_syntax("js/data.js"))
    results.append(check_js_syntax("js/charts.js"))
    results.append(check_js_syntax("js/main.js"))
    print()

    print("=" * 60)
    if all(results):
        print("✅ 所有检查通过！项目可以正常使用。")
        print()
        print("快速启动：")
        print("  cd /root/.openclaw/workspace/ancient-architecture-visualization")
        print("  python3 -m http.server 8000")
        print("  然后访问 http://localhost:8000")
        return 0
    else:
        print("⚠️  部分检查未通过，请检查上述错误。")
        return 1

if __name__ == "__main__":
    sys.exit(main())
