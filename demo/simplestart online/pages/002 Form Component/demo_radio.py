### Radio
import simplestart as ss

ss.md("## ss.radio")

ss.space()

ss.md('''
#### 🔅 Example
''')

def onchange(event):
    ss.session["options_value"] = event.value
    ss.session["options_index"] = event.index
    
ss.md("onchange: value:@options_value, index:@options_index")

options = ["Option 1", "Option 2", "Option 3"]
myradio = ss.radio(options, label = "### my radio1", index = 0, onchange = onchange)


options = [("C++", '#### <span style="color:blue">C++</span>'), 
           ("Javascript", '#### <span style="color:green">Javascript</span>'), 
           ("Python", '#### <span style="color:red">Python</span>')
          ]
ss.radio(options, inline = True, label = "### my radio2", index = 0, iconColor = "blue", onchange = onchange)



ss.write("---")
ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

def onchange(event):
    ss.session["options_value"] = event.value
    ss.session["options_index"] = event.index
    
ss.md("onchange: value:\@options_value, index:\@options_index")

options = ["Option 1", "Option 2", "Option 3"]
myradio = ss.radio(options, label = "### my radio1", index = 0, onchange = onchange)


options = [("C++", '#### <span style="color:blue">C++</span>'), 
           ("Javascript", '#### <span style="color:green">Javascript</span>'), 
           ("Python", '#### <span style="color:red">Python</span>')
          ]
ss.radio(options, inline = True, label = "### my radio2", index = 0, iconColor = "blue", onchange = onchange)

def onPageLoad():
    ss.session["options_value"] = ""

''')


ss.space()
ss.md('''
---
#### 🔅 Example - Get State Value
''')

def myclick1():
    ss.message(myradio.value)

ss.button("Get State Value", onclick=myclick1)

def myclick2():
    ss.message(myradio.index)

ss.button("Get State Index", onclick=myclick2)

ss.write("---")
ss.write("#### 🔎 Code Snippet")

ss.md('''
```python
#...
def myclick1():
    ss.message(myradio.value)

ss.button("Get State Value", onclick=myclick1)

def myclick2():
    ss.message(myradio.index)

ss.button("Get State Index", onclick=myclick2)
''')


def onPageLoad():
    ss.session["options_value"] = ""