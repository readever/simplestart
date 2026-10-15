<div align="center">

**English** | [简体中文](README_zh.md)

</div>

# SimpleStart

**Build Interactive Web Apps with Python.**

[![PyPI - Version](https://img.shields.io/pypi/v/simplestart)](https://pypi.org/project/simplestart/)
[![Python Versions](https://img.shields.io/pypi/pyversions/simplestart)](https://pypi.org/project/simplestart/)
[![Documentation](https://img.shields.io/badge/docs-simplestart.cc-blue)](http://www.simplestart.cc/)

SimpleStart is a Python framework designed for developers and data analysts who want to build reactive web apps without touching HTML, CSS, or JavaScript. It handles the complexity of modern web standards for you, allowing you to focus purely on Python logic and data.

> **Note**: This repository hosts examples, tutorials and the issue tracker for SimpleStart. The framework itself is distributed via [PyPI](https://pypi.org/project/simplestart/). Bug reports and feature requests are welcome in [Issues](https://github.com/readever/simplestart/issues).

## Online Help

- **Documentation (English)**: <http://www.simplestart.cc/>
- **文档（中文）**: <http://www.simplestart.cc/zh>

## 🚀 Why SimpleStart?

- **Event-driven — no full-page reruns**: Interactions fire targeted callbacks (`onclick`, `onchange`) that update only the affected elements. Your script is **not** re-executed from top to bottom on every click, so apps stay fast and predictable as they grow.
- **Two-way reactive binding**: Bind `ss.state` properties directly to component parameters (or `@@variable` in text). Change a value anywhere — form inputs write back too — and every bound element updates instantly. No wiring, no refreshes.
- **Pure Python, end to end**: Tables, forms, charts, layouts and media — all from Python. No HTML, CSS, JavaScript, or frontend build tools.
- **Rich, modern components**: A comprehensive built-in component library with a clean, responsive UI out of the box.

## ⚡ Quick Start

Get your first app running in 3 simple steps:

### 1. Install SimpleStart

```bash
pip install simplestart
```

### 2. Create Your App

Create a file named app.py and write your logic:

```python
import simplestart as ss

ss.write("Hello, World")

def myclick():
    ss.write("Welcome to SimpleStart.")

ss.button("Click Me", onclick=myclick)
```

Click the button and the welcome message is written to the page — pure Python, no HTML or JavaScript.

### 3. Run and Access

Run your script in the terminal:

```bash
ss app.py
```

Access your app in your browser at `http://localhost:8000`.

## 📖 Learn the Basics in 5 Examples

The [`examples/`](./examples) folder contains five tiny, complete apps — each under 30 lines. Clone this repository and run any of them:

```bash
ss examples/01_hello.py
```

| # | Example | What you'll learn |
|---|---|---|
| 1 | [01_hello.py](./examples/01_hello.py) | Write text, buttons and event callbacks |
| 2 | [02_state.py](./examples/02_state.py) | Reactive session state with `@@variable` binding |
| 3 | [03_form.py](./examples/03_form.py) | Build forms with inputs, sliders and cards |
| 4 | [04_data.py](./examples/04_data.py) | Turn Python data into tables and cards |
| 5 | [05_chart.py](./examples/05_chart.py) | Draw interactive charts with one function call |

## Demo

Here are some examples of what you can build with SimpleStart:

### Iris Classification (KNN)

A complete machine learning workflow (data exploration, training, prediction) built with SimpleStart.

👉 Try it online: [English](https://modelscope.cn/studios/simplestart/Iris_Predict) · [中文](https://modelscope.cn/studios/simplestart/Iris_Predict_cn)

## 📚 Resources

- 📖 **Documentation**: [English](http://www.simplestart.cc/) · [中文](http://www.simplestart.cc/zh)
- 📦 **PyPI**: [pypi.org/project/simplestart](https://pypi.org/project/simplestart/)
- 🐛 **Feedback**: bug reports and feature requests → [GitHub Issues](https://github.com/readever/simplestart/issues)

## License

SimpleStart is **free to use** — install it and build personal or commercial applications at no cost. It is distributed under a proprietary license (© readever) that simply asks you not to redistribute or reverse-engineer the framework itself. The examples and tutorials in this repository are provided for learning purposes. For licensing questions, open an [issue](https://github.com/readever/simplestart/issues).



