### Columns Layout
import streamsync as ss

ss.md("## ss.columns Columns Layout")

ss.space()
ss.md("#### 🔅 Example")

ss.space()

ss.md("### Average Spacing")

def onchange1(event):
    #cols_ex1.design = True
    cols_ex1_id = cols1[0].id 

    if event.value == True:
        ss.getcm().components[cols_ex1_id]["content"]["options"]["border"] = True
        ss.session["cols1_design"] = ', border = True'
    else:
        ss.getcm().components[cols_ex1_id]["content"]["options"]["border"] = False
        ss.session["cols1_design"] = ''
    ss.update_cm(cols_ex1_id)
      
ss.checkbox("border", checked = True, onchange = onchange1)

cols1 = ss.columns(2, border=True)

with cols1[0]:
    ss.text("First of two columns")

with cols1[1]:
    ss.text("Second of two columns")


ss.space()
ss.write("---")
ss.write("#### 🔎 Code")
ss.md('''
```python
import simplestart as ss

cols1 = ss.columns(2, border = True)

with cols1[0]:
    ss.text("First of two columns")
    
with cols1[1]:
    ss.text("Second of two columns")
```
''')
    
ss.space()

ss.md("### Proportional Spacing")


def onchange2(event):
    #cols_ex1.design = True
    cols_ex2_id = cols2[0].id 

    if event.value == True:
        ss.getcm().components[cols_ex2_id]["content"]["options"]["border"] = True
        ss.session["cols2_design"] = ', border = True'
    else:
        ss.getcm().components[cols_ex2_id]["content"]["options"]["border"] = False
        ss.session["cols2_design"] = ''
    ss.update_cm(cols_ex2_id)
        

ss.checkbox("border", checked = True, onchange = onchange2)

cols2 = ss.columns([4,6], border = True)

with cols2[0]:
    ss.text("First of two columns")
with cols2[1]:
    ss.text("Second of two columns")

    
ss.space()
ss.write("---")
ss.write("#### 🔎 Code")
ss.md('''
```python
import simplestart as ss

cols1 = ss.columns([4,6], border = True)

with cols1[0]:
    ss.text("First of two columns")
    
with cols1[1]:
    ss.text("Second of two columns")
```
''')

def onPageLoad():
    ss.session["cols1_design"] = ''
    ss.session["cols2_design"] = ''