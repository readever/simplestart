### Section
import simplestart as ss

ss.md("## ss.section Container")

ss.md("The section parent container can hold other components and supports the style parameter.")


ss.space()
ss.md('''
#### 🔅 Example
''')

#api
def clear():
    section.empty()
    
def write_something():
    section.text("Hello, I am inside section 2")

#ui
with ss.section("Section1", shadow = 10, border = True, rounded=True, width = "50%", height=300):
    ss.text("This is inside the section 1")
    

ss.space()    

section = ss.section()
section.text("This is inside the section 2")

ss.space("mt-4 mb-4")   
ss.text("outside the section")


ss.md("---")

ss.button("clear", onclick=clear)

ss.button("add something", onclick=write_something)

ss.space()

ss.write("#### 🔎 Code")

ss.md("""
```python
import simplestart as ss

#api
def clear():
    section.empty()
    
def write_something():
    section.text("Hello, I am inside section 2")

#ui
with ss.section(title = "Section1", shadow = 10, border = True, rounded=True, width = "50%", height=300):
    ss.text("This is inside the section 1")
    

ss.space()    

section = ss.section()
section.text("This is inside the section 2")

ss.space()   
ss.text("outside the section")

ss.md("---")

ss.button("clear", onclick=clear)
ss.button("add something", onclick=write_something)

```
""")

ss.md('''
::: tip
  In addition to adding components using the with syntax, you can also directly add components within the container using section.text(), section.button(), etc.
:::
''')