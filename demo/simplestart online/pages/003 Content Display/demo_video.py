### Video Playback
import streamsync as ss

ss.md("## ss.video Video Playback")

ss.md("Supports playing videos in formats like mp4.")

ss.md('''
#### 🔅 Example
''')

src = "https://media.w3.org/2010/05/sintel/trailer.mp4"

player = ss.video(src, style="width:50%")

ss.text("Source: https://media.w3.org/2010/05/sintel/trailer.mp4", style="color:gray")

ss.space("mt-8")

ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

src = "https://media.w3.org/2010/05/sintel/trailer.mp4"

player = ss.video(src, style="width:100%; max-width:640px")
    
#Change video source
#player.src = "..."
```
''')
