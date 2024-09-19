### Row Layout

import streamsync as ss

ss.md("## ss.row Row Layout")

ss.space()
ss.md("#### 🔅 Example")
ss.write("Use ss.row to constrain two buttons to display on the same line, while using ss.spacer to adjust the layout of the buttons.")

ss.space()

def onchange1():
    pass
    

#ui

style = "background:#d3d3d354; padding:5px;"

ss.space()
ss.write("#### 1. Normal")
ss.space()
with ss.row(style=style):
    ss.button("button1")
    ss.button("button2")

ss.space()
ss.write("#### 2. Center")
ss.space()
with ss.row(style=style):
    ss.spacer()
    ss.button("button1")
    ss.button("button2")
    ss.spacer()
    
ss.space()
ss.write("#### 3. Right align")
ss.space()
with ss.row(style=style):
    ss.spacer()
    ss.button("button1")
    ss.button("button2")
    
ss.space()
ss.write("#### 4. Right respectively")
ss.space()
with ss.row(style=style):
    ss.spacer()
    ss.button("button1")
    ss.spacer()
    ss.button("button2")
    
    
ss.space("mt-16")
ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

style = "background:#d3d3d354; padding:5px;"
ss.space()
ss.write("#### 1. Normal")
ss.space()
with ss.row(style=style):
    ss.button("button1")
    ss.button("button2")

ss.space()
ss.write("#### 2. Center")
ss.space()
with ss.row(style=style):
    ss.spacer()
    ss.button("button1")
    ss.button("button2")
    ss.spacer()
    
ss.space()
ss.write("#### 3. Right align")
ss.space()
with ss.row(style=style):
    ss.spacer()
    ss.button("button1")
    ss.button("button2")
    
ss.space()
ss.write("#### 4. Right respectively")
ss.space()
with ss.row(style=style):
    ss.spacer()
    ss.button("button1")
    ss.spacer()
    ss.button("button2")

''')

ss.md('''
::: tip
  ss.space adds spacing, while ss.spacer is used to fill gaps to modify the layout.
:::
''')