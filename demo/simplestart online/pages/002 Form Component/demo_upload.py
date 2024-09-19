### File Upload
import streamsync as ss
import pandas as pd

ss.md("## ss.upload File Upload")


ss.space()
ss.md("#### 🔅 Example - Upload Image")
ss.space()


def onsucess(event):
    filename = event.value
    path = f'{ss.baseinfo["package_path"]}/uploads/{filename}'
    myimage.image = path
    
ss.upload("Upload Image ...", accept="image/png, image/jpeg, image/bmp", icon="mdi-camera", onsucess = onsucess)

myimage = ss.image()

ss.space()
ss.write("---")
ss.write("#### 🔎 Code")

ss.md('''
```python
import simplestart as ss

def onsucess(event):
    filename = event.value
    path = f'{ss.baseinfo["package_path"]}/uploads/{filename}'

    myimage.image = path
    
ss.upload(label = "Upload Image ...", accept="image/png, image/jpeg, image/bmp", icon="mdi-camera", onsucess = onsucess)

myimage = ss.image()

''')