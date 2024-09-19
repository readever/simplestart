### Style
import simplestart as ss

ss.md("## ss.style Style Settings")

ss.space()
ss.md("#### 🔅 Example")
ss.write("nject CSS styles into the HTML document.")

ss.html('''
    <div class="test1">this is a sample1</div>
    <div class="test2">this is a sample2</div>
''')


ss.style('''
    .test1{
        background-color:lightgray;
        padding:5px;
        width:150px;
        margin-bottom:10px;
        border:1px solid lightblue
    }
    .test2{
        color:red;
        border:1px solid lightgreen;
        padding:5px;
        width:150px;
    }
''')

ss.space()

ss.write("#### 🔎 Code")


ss.space()


ss.md('''
```python
import simplestart as ss

ss.html(\'''
    <div class="test1">this is a sample1</div>
    <div class="test2">this is a sample2</div>
\''')

ss.style(\'''
    .test1{
        background-color:lightgray;
        padding:5px;
        width:150px;
        margin-bottom:10px;
        border:1px solid lightblue
    }
    .test2{
        color:red;
        border:1px solid lightgreen;
        padding:5px;
        width:150px;
    }
\''')
''')
