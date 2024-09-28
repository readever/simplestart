<h4 align="center">
    <p>
        <a href="https://github.com/readever/simplestart/blob/main/README.md">English</a> |
        <b>中文（简体）</b>
    <p>
</h4>

# SimpleStart
SimpleStart - 使用 Python 轻松实现网页开发和数据可视化，是 Streamlit 的替代方案。

## 什么是 SimpleStart
SimpleStart 旨在服务于初学者和经验丰富的开发者。它是一个强大的工具，可以使用 Python 在后端进行网页应用开发，无需前端编程知识。您可以轻松创建丰富的应用程序，而无需任何 HTML、CSS、JavaScript 或 Ajax 技能。

它提供多种组件，如文本、按钮、列表、表格、音频和视频，并具备可定制的布局。此外，SimpleStart 还支持通过图像、表格和图表进行数据可视化。

## 主要特性

- 支持事件响应和数据驱动应用
- 轻松支持多页面应用
- 丰富的组件集，能够创建自定义组件
- 数据可视化和图表
- 快速安装、开发、调试和部署

## 入门指南

### 安装

```bash
pip3 install simplestart
```

### 运行示例
```bash
ss app.py
```
或者
```bash
ss app.py --port 8000
```

## 快速开始

以下是一个简单示例，演示如何使用 SimpleStart 创建基本网页应用:

```python
import simplestart as ss

def myclick(event):
    ss.message("clicked")

ss.write("Hello, world")
ss.button("Test", onclick=myclick)
```

## 效果展示

### 1. 按钮和事件处理
![按钮样式和事件处理](./resource/ezgif-button.gif)

## 链接

- **主页**: <a href="http://www.simplestart.cc/zh" rel="nofollow" target="_blank">SimpleStart 主页</a> 访问主页获取有关 SimpleStart 的更多信息.
- **在线演示**:  <a href="http://demo.simplestart.cc/demo01" rel="nofollow" target="_blank">SimpleStart Online Demo</a> 在线演示，体验 SimpleStart 的功能.
- **机器学习示例**:  <a href="http://demo.simplestart.cc/demo02" rel="nofollow" target="_blank">Iris Classification Demo</a> 机器学习示例，了解如何在该领域应用 SimpleStart.
- **演示源代码**: 所有演示代码也包含在这个 GitHub 仓库中.
