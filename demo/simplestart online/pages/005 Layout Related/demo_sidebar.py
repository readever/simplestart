### Sidebar
import simplestart as ss

ss.md("## ss.sidebar")

ss.md("Display various components in the sidebar on the left side of the screen, such as data controls and some settings.")

ss.md('''
#### 🔅 Example
''')


sidebar = ss.sidebar()

with sidebar:
    ss.button("click")
    ss.selectbox(["one", "two", "three"])
        

def testme(state, value):
    with sidebar:
        ss.text("text in sidebar")

    
ss.button("test", onclick = testme)


ss.space()

ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

sidebar = ss.sidebar()

with sidebar:
    ss.button("click")
    ss.selectbox(["one", "two", "three"])
        

def testme(state, value):
    with sidebar:
        ss.text("text in sidebar")
    #or
    #sidebar.text("text in sidebar")

    
ss.button("test", onclick = testme)

```
''')