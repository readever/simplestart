<div align="center">

[English](README.md) | **简体中文**

</div>

# SimpleStart

**用纯 Python 构建交互式 Web 应用。**

[![PyPI - Version](https://img.shields.io/pypi/v/simplestart)](https://pypi.org/project/simplestart/)
[![Python Versions](https://img.shields.io/pypi/pyversions/simplestart)](https://pypi.org/project/simplestart/)
[![Documentation](https://img.shields.io/badge/docs-simplestart.cc-blue)](https://www.simplestart.cc/zh)

SimpleStart 是一个 Python 框架，面向希望不接触 HTML、CSS、JavaScript 就能构建响应式 Web 应用的开发者和数据分析师。它为你处理现代 Web 标准的复杂性，让你专注于 Python 逻辑和数据。

> **说明**：本仓库托管 SimpleStart 的示例、教程和 Issue 跟踪。框架本身通过 [PyPI](https://pypi.org/project/simplestart/) 分发。欢迎在 [Issues](https://github.com/readever/simplestart/issues) 提交 Bug 报告和功能建议。

## 在线帮助

- **文档（中文）**：<https://www.simplestart.cc/zh>

- **Documentation (English)**: <https://www.simplestart.cc/>

## 🚀 为什么选择 SimpleStart？

- **事件驱动，无整页重跑**：交互触发精准的回调（`onclick`、`onchange`），只更新受影响的元素。你的脚本**不会**在每次点击时从上到下重新执行，应用规模变大后依然快速、可预期。

- **双向响应式绑定**：将 `ss.state` 属性直接绑定到组件参数（或在文本中使用 `@@variable`）。在任何地方修改值——表单输入也会回写——所有绑定的元素立即更新。无需手工接线，无需刷新。

- **纯 Python，贯穿始终**：表格、表单、图表、布局和媒体——全部用 Python 完成。无需 HTML、CSS、JavaScript，无需前端构建工具。

- **丰富、现代的组件库**：内置完善的组件库，开箱即得干净、响应式的界面。

## ⚡ 快速开始

3 步跑起你的第一个应用：

### 1. 安装 SimpleStart

```bash
pip install simplestart

```

### 2. 创建应用

创建名为 app.py 的文件，写下你的逻辑：

```python
import simplestart as ss

ss.write("Hello, World")

def myclick():
    ss.write("Welcome to SimpleStart.")

ss.button("Click Me", onclick=myclick)

```

点击按钮，欢迎消息就会写入页面——纯 Python，无需 HTML 或 JavaScript。

### 3. 运行并访问

在终端运行脚本：

```bash
ss app.py

```

在浏览器访问 `http://localhost:8000` 。

## 📖 5 个例子学会基础

[`examples/`](./examples) 目录包含五个短小完整的示例应用——每个不超过 30 行。克隆本仓库即可运行：

```bash
ss examples/01_hello.py

```

| # | 示例 | 学习内容 |
|---|---|---|
| 1 | [01_hello.py](./examples/01_hello.py) | 文本写入、按钮与事件回调 |
| 2 | [02_state.py](./examples/02_state.py) | 响应式状态与 `@@variable` 绑定 |
| 3 | [03_form.py](./examples/03_form.py) | 用输入框、滑块和卡片构建表单 |
| 4 | [04_data.py](./examples/04_data.py) | 把 Python 数据变成表格和卡片 |
| 5 | [05_chart.py](./examples/05_chart.py) | 一次函数调用绘制交互式图表 |

## 演示

以下是用 SimpleStart 构建的应用示例：

### 鸢尾花分类（KNN）

一个完整的机器学习工作流（数据探索、训练、预测），使用 SimpleStart 构建。

👉 在线体验：[English](https://modelscope.cn/studios/simplestart/Iris_Predict) · [中文](https://modelscope.cn/studios/simplestart/Iris_Predict_cn)

## 📚 资源

- 📖 **文档**：[中文](https://www.simplestart.cc/zh) · [English](https://www.simplestart.cc/)

- 📦 **PyPI**：[pypi.org/project/simplestart](https://pypi.org/project/simplestart/)

- 🐛 **反馈**：Bug 报告与功能建议 → [GitHub Issues](https://github.com/readever/simplestart/issues)

## 许可证

SimpleStart **免费使用**——安装后即可构建个人或商业应用，无需任何费用。框架以专有许可发布（© readever），仅要求不二次分发、不逆向工程框架本身。本仓库中的示例和教程仅供学习使用。许可相关问题请提交 [issue](https://github.com/readever/simplestart/issues) 。
