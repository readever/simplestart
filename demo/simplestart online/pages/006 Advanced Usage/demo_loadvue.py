### ss.loadvue
import simplestart as ss

ss.md("## ss.loadvue Load Vue SFC")

ss.space()
ss.md("In SimpleStart, you can load custom Vue Single File Components using ss.loadvue, enabling property and data interaction.")

ss.space()

ss.space()
ss.md('''
#### 🔅 Example

In this example, we define a simple frontend component that includes an "ontest" event. When the user clicks the "handle on server" button, 
the Python side's ontest event handler will process it and receive data passed from the frontend component. Meanwhile, when the "Modify Data" 
button on the Python side is clicked, the frontend component will respond by changing the displayed content.
''')

ss.space("mt-8")
ss.md("---")
ss.space("mt-8")

tagid = 0
tags = ["Python", "Java", "Javascript"]
data = {"count":0, "language":"C++"}
global myvue

#trigger event on server from client side
def ontest(event):
    ss.message(event.value)

#change data in client component on server side
def changedata(event):
    global tagid
    myvue.data["language"] = tags[tagid]
    myvue.update()
    
    tagid = (tagid+1) % 3
    
ss.text("Python Side")
ss.button("Modify Data", onclick=changedata)

ss.space()
sec = ss.section()

def onPageLoad():
    global myvue
    #load code from file
    with sec:
        ss.text("Component Side")
        myvue = ss.loadvue(path = "components/mycomponent.vue", data = data, handlers = {"ontest":ontest})
    
    
ss.space()
ss.write("Python Side Code")

ss.md('''
```python
import simplestart as ss

tagid = 0
global myvue

tags = ["Python", "Java", "Javascript"]
data = {"count":0, "language":"C++"}


#trigger event on server from client side
def ontest(state, value):
    ss.message(value)

#change data in client component on server side
def changedata(state, value=None):
    global tagid
    myvue.data["language"] = tags[tagid]
    tagid = (tagid+1) % 3
    
ss.text("Python Side")
ss.button("Modify Data", onclick=changedata)


def onPageLoad():
    global myvue
    #load code from file
    myvue = ss.loadvue(path = "components/mycomponent.vue", data = data, handlers = {"ontest":ontest})
```
''')


ss.space()
ss.write("Vue JS Code")

ss.md('''
```js
<template>
  <div class="my-component">
    <h1>{{title}}: {{ data.language }}</h1>
    <v-btn @click="testme">handle on server</v-btn>
  </div>
</template>

<script>
module.exports = {
    name: 'MyComponent',

    data() {
        return {
            title:"computer",
        }
    },

    methods: {
        testme(){
            this.streamsync.forwardData(this, eventname="ontest", "12345")
        }
    }
}
</script>

<style>
.my-component {
    width:50%;
    background-color: #f0f0f0;
    padding: 20px;
    margin:10px 0;
}
</style>

```
''')