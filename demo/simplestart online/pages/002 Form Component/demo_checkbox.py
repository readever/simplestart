### Checkbox
import simplestart as ss

ss.write("### ss.checkbox")

def onchange(event):
    ss.session["checked_value"] = event.value


ss.md('''
---
#### 🔅 Example 1
''')

ss.md("onchange: @checked_value")

ss.checkbox("checkme", onchange = onchange)
ss.checkbox("initially checked", checked = True, onchange = onchange)


ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

def onchange(state, value):
    state["checked_value"] = value

#ui
ss.md("onchange: @checked_value")

ss.checkbox("checkme", onchange = onchange)
ss.checkbox("initially checked", checked = True, onchange = onchange)


''')

ss.space()
ss.md('''
---
#### 🔅 Example 2
Get the status of the checkbox
''')

mycheck = ss.checkbox("check me", onchange = onchange)

def myclick():
    ss.message(mycheck.value)

ss.button("Get Status", onclick = myclick)

ss.space()
ss.write('''
---
#### 🔎 Code
''')


ss.md('''
```python
import simplestart as ss

mycheck = ss.checkbox("check me", onchange = onchange)

def myclick():
    ss.message(mycheck.value)

ss.button("获取状态", onclick = myclick)

''')

def onPageLoad():
    ss.session["checked_value"] = ""