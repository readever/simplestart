### Selectbox
import simplestart as ss

ss.md("## ss.selectbox")

ss.space()
ss.md('''
#### 🔅 Example 1
Create a selectbox with a title and 3 options on the page.
''')
ss.space()

options = ["option1","option2", "option3"]

def selchange(event):
    ss.message(f"You select {event.value}, index of {event.index}")

select1 = ss.selectbox(options, index=0, title = "### Please select", onchange = selchange)



ss.write("#### 🔎 Code")

ss.md("""
```python
import simplestart as ss

options = ["option1","option2", "option3"]

def selchange(event):
    ss.session["select_value"] = event.value
    ss.session["select_index"] = select1.index

ss.write("info value:  index:")
select1 = ss.selectbox(options, value="option1", onchange = selchange)


```
""")

ss.md('''
#### 🔅 Example 2
Get the current option of the selectbox. In addition to obtaining the user's selected option information through the event's index and value in the selectbox's onchange event, you can also get the user's selection information via the selectbox variable.
''')
ss.space()

def onclick1():
    ss.message(select1.value)
    
ss.button("Current Option Value", onclick=onclick1)

def onclick2():
    ss.message(select1.index)
    
ss.button("Current Option Index", onclick=onclick2)

ss.space()

ss.write("#### 🔎 Code Snippet")


ss.md("""
```python

#...

def onclick1():
    ss.message(select1.value)
    
ss.button("Current Option Value", onclick = onclick1)

def onclick2():
    ss.message(select1.index)
    
ss.button("Current Option Index", onclick = onclick2)

```
""")