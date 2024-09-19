### Message
import simplestart as ss

ss.md("## ss.message Popup Message")

ss.space()


ss.md('''
#### 🔅 Example 
''')
ss.space()


def showmsg():
    ss.message("Hello, world")

showmsg()
ss.button("message", onclick=showmsg)


ss.space("mt-8")

ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

def showmsg():
    ss.message("Hello, the world")

```
''')