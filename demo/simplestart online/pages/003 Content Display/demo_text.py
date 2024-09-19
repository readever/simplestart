### Text
import streamsync as ss

ss.md("## ss.text Text")
ss.md("Supports the style parameter.")


ss.space()
ss.space()
ss.md('''
#### 🔅 Example
''')

ss.md("---")

#Basic usage
test = ss.text("hello, world")

#Change color
ss.text("This is a red string", style="color:red")

ss.space()
ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

#Basic usage
test = ss.text("hello, world")

#Change color
ss.text("This is a red string", style="color:red")
```
''')