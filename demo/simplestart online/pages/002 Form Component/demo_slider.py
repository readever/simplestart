### Slider
import simplestart as ss

ss.md("## ss.slider")

ss.space()

ss.md('''
#### 🔅 Example 
''')

ss.md("### Please drag the slider to change the value")

info = ss.text("number")

def onchange(event):
    info.text = event.value

ss.slider("<b>my slider</b>", value=500, min=0, max=1000, onchange=onchange, style="width:50%")

ss.space()

ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

info = ss.text("number")

def onchange(state, value):
    info.text = value

ss.slider(500, 0, 1000, onchange=onchange)
''')
