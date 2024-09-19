### Text_input
import streamsync as ss


ss.md("## ss.text_input")

ss.space()
ss.md("#### 🔅 Example")

ss.md("---")
ss.space()

def onchange(state, value):
    ss.message(f"onchange, {value}")

def onclear(state, value):
    ss.message("onclear event happend")

def onblur(state, value):
    print("onblur")
    ss.message(f"onblur, {value}")
    
def testme():
    ss.message(myinput.value)
    
#ui
cols = ss.columns([50,50], border = True)
with cols[0]:
    myinput = ss.text_input("Hello SimpleStart", clearable=True)


def myevent(event):
    if event.tag == "sel1":
        myinput.variant = event.value
    elif event.tag == "sel2":
        myinput.type = event.value
    elif event.tag == "but1":
        ss.message(myinput.value)
    

with cols[1]:
    ss.selectbox(["filled","outlined","underlined", "solo", "solo-filled", "solo-inverted"], label='#### <span style = "color:green">Change the input style</span>', \
                value="solo", onchange = myevent, eventTag="sel1")
    
    ss.selectbox(["text","time", "date", "week", "month", "password",  "color"], label='#### <span style = "color:green">Change the input type</span>', \
                onchange = myevent, eventTag="sel2")
 
    ss.write('#### <span style="color:green">Get Input Value</span>')
    ss.button("Get Text Value", onclick=myevent, eventTag="but1")



ss.write("---")
ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

myinput = ss.text_input("Hello SimpleStart", clearable=True)

#Or
#ss.text_input("hello", type="text", variant = "filled")

''')