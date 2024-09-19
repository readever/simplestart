### ss.component
import simplestart as ss

ss.md("### ss.component Custom Component")
ss.md("You can customize components using HTML, JS, and CSS, implemented through an iframe.")

ss.space()
ss.md('''
#### 🔅 Example
''')
ss.space()

def testme(state, value):
    mytext.text = "Data received from the frontend UI: " + value["value"]
    
# By default, the <iframe> width is 300 pixels and the height is 150 pixels.
ss.text("Enter content in the text box and press Enter.")

myplugin = ss.component(path = f"components/index.html", onData = testme) ###style="border:none")

def postdata():
    data = {"my_input_value":"text from python"}
    myplugin.postMessage(data)

mytext = ss.text("Data received from the frontend UI: ")

ss.markdown("---")
ss.space()
ss.text("Click the button to send data to the frontend UI.")
ss.button("post data", onclick=postdata)

ss.space()

ss.write("Python Side Code")

ss.md('''
```python
import simplestart as ss

def testme(state, value):
    mytext.text = "Data received from the frontend UI: " + value["value"]
    
ss.text("Enter content in the text box and press Enter.")
myplugin = ss.component(path = f"components/index.html", onData = testme)

def postdata():
    data = {"my_input_value":"text from python"}
    myplugin.postMessage(data)

mytext = ss.text("Data received from the frontend UI: ")

ss.markdown("---")

ss.space()
ss.text("Click the button to send data to the frontend UI.")
ss.button("post data", onclick=postdata)

```
''')

ss.write("Plugin/HTML/JS Side Code")

ss.md('''
```html
<html>
    
<head>
    <script src="pybridge.js"></script>
</head>
    
<body style="height:100px">
    <input id="myinput" value="" autocomplete="off" placeholder="Enter content and press Enter" />
</body>
    
<script>
    var myInput = document.getElementById("myinput");

    myInput.addEventListener("change", function() {
        //// Send message to the Python side
        sendDataToPython({
            value: myInput.value,
        });
    })
    
    //Receive messages from the Python side
    window.addEventListener("message", onDataFromPython);
    
    function onDataFromPython(event) {
        var data = event.data.arg;
        if (event.data.type !== "ss:render") return;
            myInput.value = data.my_input_value;  // Access values sent from Python here!
    }
    
    // If system height setting fails, you can manually set the height
    //setFrameHeight(200);
</script>

</html>

```
''')