### Textarea
import streamsync as ss

ss.md("## ss.textarea")

ss.space()
ss.md("#### 🔅 Example")

ss.md("---")

# Basic usage
# test = ss.text_input("hello, world", type="textarea")
mytext = ss.textarea("hello, world")

ss.write("---")
ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

mytext = ss.textarea("hello, world")

''')

ss.space()
ss.md("#### 🔅 Get the text value of the textarea")
ss.md("---")

def myclick():
    ss.message(mytext.value)
    
ss.button("Get Text", onclick=myclick)

ss.write("---")
ss.write("#### 🔎 Code Snippet")

ss.md('''
```python
#...
def myclick():
    ss.message(mytext.value)
    
ss.button("Get Text", onclick=myclick)
''')
