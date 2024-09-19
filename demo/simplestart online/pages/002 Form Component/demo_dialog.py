### Dialog
import simplestart as ss

ss.md("## ss.dialog")

ss.space()

ss.md('''
---
#### 🔅 Example
''')

def testme():
    ss.message("testme")
    
def showit():
    if ss.session["str_fullscreen"] != "":
        dialog.show(fullscreen = True)
    else:
        dialog.show()
    
def myclose(event):
    ss.message("dialog close with result " + event.value)
    
dialog = ss.dialog("Dialog Title",  onclose=myclose)
with dialog:
    ss.text("SimpleStart dialog demostration")
    ss.md("---")
    ss.button("testme", onclick=testme)
    ss.md(":smile:")
        
cols = ss.columns([60,"flex:40; border-left:1px solid lightgray"], border=True, style="border:1px solid lightgray")
with cols[0]:
    mytext = ss.text("This is dialog")
    ss.button("show dialog", onclick=showit)
    
def mycheck(event):
    if event.value == True:
        ss.session["str_fullscreen"] = "fullscreen = True"
        #dialog.show(fullscreen = True)
    else:
        ss.session["str_fullscreen"] = ""

with cols[1]:
    ss.text("Dialog Options")
    ss.checkbox("Fullscreen", onchange=mycheck)

ss.space()
ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

def myclose(event):
    ss.message("dialog close with result " + event.value)
    
dialog = ss.dialog(title="Dialog Title", onclose=myclose)
with dialog:
    ss.text("Opening from the bottom")
    ss.md("---")
    ss.button("testme", onclick=testme)
    ss.md(":smile:")
    
def showit():
    dialog.show(@str_fullscreen)
    
ss.button("show dialog", onclick=showit)
```
''')

def onPageEnter():
    ss.session["str_fullscreen"] = ""
    
    
