### Html Hypertext
import streamsync as ss


ss.md("## ss.html")

ss.space("")

ss.md('''
#### 🔅 Example
''')


ss.md("### html")

ss.html(f"""
    <p>This is a piece of rich text content, which contains <strong>bold</strong> and <em>italic</em> text.</p>
    <style>
    .testclass{{
        color:red;
        font-weight:bold;
    }}
    </style>
    <div class="testclass">this is red</div>
""")

ss.space("mt-8")

ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

ss.html(f"""
    <p>This is a piece of rich text content, which contains <strong>bold</strong> and <em>italic</em> text.</p>
    <style>
    .testclass{{
        color:red;
        font-weight:bold;
    }}
    </style>
    <div class="testclass">this is red</div>
""")
```
''')