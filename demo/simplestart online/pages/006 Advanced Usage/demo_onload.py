### ss.onPageEnter
import simplestart as ss
from datetime import datetime

ss.md("## onPageEnter Page Load Event")

ss.md('''
---
#### 🔅 Example
''')

ss.md("Every time you enter this page, the onPageEnter event function will be called, and a message will pop up above.")


ss.space()

mytext = ss.text("Current Time @currentime")

def onPageEnter():
    #ss.write("test")
    ss.message("page enter event") 


    # Get current time
    now = datetime.now()
    # Format time as a string
    time_str = now.strftime('%Y-%m-%d %H:%M:%S')    
    ss.session["currentime"] = time_str


ss.space()

ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

def onPageEnter():
    ss.message("page enter event")

```
''')