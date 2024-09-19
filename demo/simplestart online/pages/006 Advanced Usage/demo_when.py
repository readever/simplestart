### ss.when
import simplestart as ss

ss.md('''
## ss.when onditional Statements
''')

ss.space()
ss.md('''
#### 🔅 Example
''')

#api
def increment(event):
    ss.session["counter"] += 1
    
def decrement(event):
    ss.session["counter"] -= 1

    
#conditional func
def conditioner(event):
    #print("event", event)
    if event["flag"] == 1:
        if ss.session["counter"] >= 5:
            return True
        else:
            return False
    elif event["flag"] == 2:
        return (ss.session["viewcode"] == 1)
        

# State initialisation
ss.session["counter"] = 0
ss.session["viewcode"] = 0

#ui
ss.text("The count is @counter.")

ss.button("Increment", onclick=increment)
ss.button("Decrement", onclick=decrement)

ss.write("New content will appear below when the counter is greater than 5.")

with ss.when(conditioner, flag = 1): # Conditional rendering
    ss.text("Well done on reaching 5 👋🌷🍾")
    
ss.write("When the counter is less than 5, the new content will be hidden.")


ss.space()

ss.write("#### 🔎 Code")
ss.write("---")

def viewcode():
    ss.session["viewcode"] = 1

ss.button("View Code", size="small", onclick = viewcode)

with ss.when(conditioner, flag = 2):
    ss.md('''
```python
import simplestart as ss

#api
def increment(event):
    ss.session["counter"] += 1
    
def decrement(event):
    ss.session["counter"] -= 1

    
#conditional func
def conditioner(event):
    return (ss.session["counter"] >= 5)
        
# State initialisation
ss.session["counter"] = 0
ss.session["viewcode"] = 0

#ui
ss.text("The count is @counter.")

ss.button("Increment", onclick=increment)
ss.button("Decrement", onclick=decrement)

ss.write("New content will appear below when the counter is greater than 5.")

with ss.when(conditioner, flag = 1): # Conditional rendering
    ss.text("Well done on reaching 5 👋🌷🍾")
    
ss.write("When the counter is less than 5, the new content will be hidden.")
```
    ''')

ss.md('''
::: tip
  The code view above is also implemented using ss.when.
:::
''')