### Tabs
import simplestart as ss

ss.md("## ss.tabs")

ss.space("mt-16")
ss.md("#### 🔅 Example")

tabtitles = ["tab1", "tab2", "tab3"]
tabs = ss.tabs(tabtitles)

with tabs[0]:
    ss.text("this is tab 1")
with tabs[1]:
    ss.text("this is tab 2")
with tabs[2]:
    ss.text("this is tab 3")
    
ss.space()
ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

tabtitles = ["tab1", "tab2", "tab3"]
tabs = ss.tabs(tabtitles)

with tabs[0]:
    ss.text("this is tab 1")
with tabs[1]:
    ss.text("this is tab 2")
with tabs[2]:
    ss.text("this is tab 3")
''')
