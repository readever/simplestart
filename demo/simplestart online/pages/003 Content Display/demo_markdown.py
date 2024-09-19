### Markdown
import simplestart as ss

ss.md("## ss.markdown")

ss.space()

ss.md('''
#### 🔅 Example 
''')

ss.space()

ss.markdown("- 19^th^")
ss.markdown("# Heading 1")
ss.markdown("## Heading 2")
ss.markdown("### Heading 3")

#Horizontal Divider
ss.markdown("---")

ss.markdown('''
- list item1
- list item2
- list item3
''')

ss.markdown(":smile:")



ss.space("mt-8")

ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

ss.markdown("# Heading 1")
ss.markdown("## Heading 2")
ss.markdown("### Heading 3")

#Horizontal Divider
ss.markdown("---")

ss.markdown(\'''
- list item1
- list item2
- list item3
\''')

```
''')