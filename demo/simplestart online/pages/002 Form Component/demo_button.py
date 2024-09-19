### Button
import streamsync as ss


ss.md('''
## ss.button
''')
ss.md('''
[Online Help](http://www.simplestart.cc)
''')
ss.space()
ss.md('''
#### 🔅 Example
''')

#Custom Function
def myclick():
    mytext.text = "You clicked "
    
def reset():
    mytext.text = "This is button"
    but1.type = ""
    ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
    ss.getcm().components[but1.id]["content"]["options"]["endicon"] = ""
    ss.getcm().components[but1.id]["content"]["options"]["icon_color"] = "mediumseagreen"
    ss.getcm().components[but1.id]["content"]["options"]["style"] = "background-color:initial;color:initial"
    ss.session["iconstr"] = ''
    ss.session["style_str"] = ''
    ss.session["style"] = ''

    
#Basic Usage
cols = ss.columns([40,"flex:60"], design=True)
with cols[0]:
    mytext = ss.text("This is button")
    but1 = ss.button("Click it", icon = "mdi-account-circle", onclick=myclick)

def onradiochange(event):
    value = event.value
    if value == "default":
        but1.type = ""
        ss.session["buttonstyle"] = ""
    elif value == "outlined":
        but1.type = "outlined"
        ss.session["buttonstyle"] = 'type = "outlined\",'
    elif value == "flat":
        but1.type = "tonal"
        ss.session["buttonstyle"] = 'type = "flat\",'
    elif value == "text":
        but1.type = "text"
        ss.session["buttonstyle"] = 'type = "text\",'
    elif value == "plain":
        but1.type = "plain"
        ss.session["buttonstyle"] = 'type = "plain\",'

def oncheckbox_change(state, value):
    if value == True:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = "aim"
        ss.session["iconstr"] = ' icon="search",'
    else:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
        ss.session["iconstr"] = ''
    but1.update()

def onradiochange2(event):
    index = event.index

    if index == 0:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = "mdi-account-circle"
        ss.getcm().components[but1.id]["content"]["options"]["endIcon"] = ""
        ss.session["iconstr"] = ' icon="mdi-account-circle",'
    elif index == 1:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
        ss.getcm().components[but1.id]["content"]["options"]["endIcon"] = "mdi-alert"
        ss.session["iconstr"] = ' endIcon="mdi-alert",'
    else:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
        ss.getcm().components[but1.id]["content"]["options"]["endIcon"] = ""
        ss.session["iconstr"] = ''
    but1.update()

    
def changeColor(bkcolor):
    ss.getcm().components[but1.id]["content"]["options"]["style"] = f"background-color:{bkcolor}; color:white"
    ss.getcm().components[but1.id]["content"]["options"]["icon_color"] = "white"
    ss.session["style_str"] = f'style="background-color:{bkcolor}, color:white"'
    ss.session["style"] = 'style=style,'
    but1.update()


with cols[1]:
    ss.text("Test")

    ss.write("---")
    ss.radio(["default", "outlined", "flat", "text", "plain"], "default", inline = True, onchange=onradiochange)

    ss.write("---")
    ss.radio([(1, "Icon(Prepend)"), (2, "Icon(Append)"), (3, "No Icon")], inline = True, onchange=onradiochange2)
    
    
    ss.write("---")
    ss.button("", type = "flat", size = "small", style="background-color:#409eff", onclick=lambda:changeColor('#409eff'))
    ss.button("", type = "flat", size = "small", style="background-color:#67c23a", onclick=lambda:changeColor('#67c23a'))
    ss.button("", type = "flat", size = "small", style="background-color:#e6a23c", onclick=lambda:changeColor('#e6a23c'))
    ss.button("", type = "flat", size = "small", style="background-color:#f56c6c", onclick=lambda:changeColor('#f56c6c'))
    ss.button("", type = "flat", size = "small", style="background-color:#909399", onclick=lambda:changeColor('#909399'))
    
    
    ss.space()
    ss.button("Reset", onclick=reset)


ss.space("mt-8")

ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

def clickme():
    mytext.text = "You clicked"
    
mytext = ss.text("This is button")
@style_str
ss.button("Click it", @buttonstyle @iconstr @style onclick=clickme)
```
''')

ss.md('''
::: tip
  Function Call
  ss.button(label, type, color, size, icon, onclick)   
:::
''')

def onPageLoad():
    ss.session["buttonstyle"] = ""
    ss.session["iconstr"] = ""
    ss.session["style"] = ""
    ss.session["style_str"] = ""
    
