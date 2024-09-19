### Audio Playback
import streamsync as ss

ss.md("## ss.audio")


ss.space()
ss.md('''
#### 🔅 Example
''')

ss.space()

audiosrc = "media/test.wav"
player = ss.audio(audiosrc)


ss.space("mt-8")

ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

audiosrc = "media/davide_quatela--breathing_barcelona.mp3"
player = ss.audio(audiosrc)
```
''')


ss.md('''
::: tip
ss.audio supports audio formats including wav, mp3, etc.
:::
''')