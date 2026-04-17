# SimpleStart

**Build Interactive Web Apps with Python.**

SimpleStart is a Python framework designed for developers, data analysts, and engineers who want to build reactive web applications without writing HTML, CSS, or JavaScript. It abstracts away the complexity of modern web standards, allowing you to focus purely on Python logic and data.

## Online Help

Visit website for more demos and examples: <http://www.simplestart.cc>


## 🚀 Key Features

- **Pure Python Development**: Build fully functional web interfaces using only Python code. No frontend build tools or knowledge required.
- **Reactive Data Binding**: The UI automatically updates when your Python variables change, making state management effortless.
- **Rich Component Library**: Comes with a comprehensive set of pre-built components including tables, forms, buttons, layouts, and media elements.
- **Event-Driven Architecture**: easily handle user interactions with simple `onclick` and `onchange` bindings.
- **Modern Web Standards**: Built on top of modern web technologies to ensure high performance and a native-like user experience.


## ⚡ Quick Start

Get your first app running in 3 simple steps:

### 1. Install SimpleStart

```bash
pip install simplestart
```

### 2. Create Your App

Create a file named app.py and write your logic:

```python
from simplestart import *

# Create a simple input and output
name = input("What is your name?")
write(f"Hello, {name}!")
```

### 3. Run and Access

Run your script in the terminal:

```bash
python app.py
```

Access your app in your browser at `http://localhost:8000`.


## License

MIT
This project is licensed under the MIT License.
