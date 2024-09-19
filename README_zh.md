<h4 align="center">
    <p>
        <a href="[readme](https://github.com/readever/simplestart/blob/main/README.md">English</a> |
        <b>中文（简体）</b>
    <p>
</h4>

# SimpleStart
SimpleStart - Easily implement web development and data visualization with Python, an alternative to Streamlit.

## What is SimpleStart
SimpleStart is designed for both beginners and experienced developers. It is a powerful tool that enables web application development using Python in the backend, without requiring front-end programming knowledge. You can easily create rich applications without any HTML, CSS, JavaScript, or Ajax skills.

It offers a variety of components like text, buttons, lists, tables, audio, and video, with customizable layouts. Additionally, SimpleStart supports data visualization through images, tables, and plot charts.

## Key Features

- Supports event response and data-driven applications
- Easily supports multi-page applications
- Rich set of components with the ability to create custom ones
- Data visualizations and charts
- Quick installation, development, debugging, and deployment

## Getting Started

### Installation

```bash
pip3 install simplestart
```

### Run Example
```bash
ss app.py
```
or
```bash
ss app.py --port 8000
```

## Quickstart

Here’s a simple example demonstrating how to create a basic web application using SimpleStart:

```python
import simplestart as ss

def myclick(event):
    ss.message("clicked")

ss.write("Hello, world")
ss.button("Test", onclick=myclick)
```

## Links

- **Home Page**: Visit our official website at [http://www.simplestart.cc](http://www.simplestart.cc) for more information about SimpleStart.
- **Online Demo**: Explore our online demo at [http://demo.simplestart.cc/demo01](http://demo.simplestart.cc/demo01) to see SimpleStart in action.
- **Machine Learning Example**: Check out a machine learning example at [http://demo.simplestart.cc/demo02](http://demo.simplestart.cc/demo02) to see how SimpleStart can be applied in this domain.
- **Source Code**: All demo code is also included in this GitHub repository.
