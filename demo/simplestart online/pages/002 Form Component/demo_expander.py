### Expander
import streamsync as ss

ss.md("## ss.expander")

ss.md('''
#### 🔅 Example
''')

with ss.expander("About SimpleStart", expanded=True):
    ss.text("Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! \
    Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!", style="padding:10px")

ss.space()
ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

with ss.expander("About SimpleStart"):
    ss.text("Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! \
    Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!")

```
''')