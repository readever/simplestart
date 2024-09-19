### Image
import simplestart as ss

import cv2
from PIL import Image
import os

ss.md("## ss.image")

ss.md('''
#### 🔅 Example
''')

ss.space()

style = "width:200px;height:200px;margin:10px"
img = "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"

cols = ss.columns([60,"flex:40"], border=True)
with cols[0]:
    mytext = ss.text("This is image")
    ss.space()
    myimg = ss.image(img, style=style, fit="contain")
    ss.text("Image fit mode: fill")
    
def onradiochange(event):
    #ss.message(event.value)
    ss.session["fit_str"] = event.value
    ss.getcm().components[myimg.id]["content"]["options"]["fit"] = event.value
    myimg.update()

def onradiochange2(event):
    value = event.value
    index = event.index


    source = ["Http", "PIL", "OpenCV", "Local"]
    ss.session["source_str"] = source[index]

    
    if index == 0:
        img = "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
        ss.session["image_path"] = "\"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg\""
        myimg.image = img
    if index == 1:
        image = Image.open('./media/image/dalao.jpeg')
        ss.session["image_path"] = "Image.open('./media/image/dalao.jpeg')"
        myimg.image = image
    if index == 2:
        img = cv2.imread('./media/image/cat.jpeg',cv2.IMREAD_COLOR)
        ss.session["image_path"] = "cv2.imread('./media/image/cat.jpeg',cv2.IMREAD_COLOR)"
        myimg.image = img  
    if index == 3:
        file_path = './media/image/dog.jpeg'
        ss.session["image_path"] = "'./media/image/dog.jpeg'"
        myimg.image = file_path
        
    myimg.update()

    
with cols[1]:
    ss.text("image fit mode")
    ss.radio(["fill", "contain", "cover", "none", "scale-down"], index = 1, inline = True, onchange=onradiochange)
    ss.space()
    ss.text("image source")
    ss.radio(["Http image","PIL image", "OpenCV image", "Local image"], index = 0, inline = True, onchange=onradiochange2)
    
ss.space()

ss.write('''
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss
import cv2
from PIL import Image

style = "width:100px; height:100px; margin:10px"
img = "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
ss.image(img, style=style, fit="fill")
```
''')



def onPageLoad():
    ss.session["info"] = "x"
    ss.session["fit_str"] = "fill"
    ss.session["source_str"] = "Http"
    ss.session["image_path"] = "\"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg\""
