'''
SimpleStart Basics 1/5: write + button + event callback
Run: ss examples/01_hello.py
'''

import simplestart as ss

ss.write("## Hello, SimpleStart!")
ss.write("Click the button and a message will be written to the page.")

def myclick():
    ss.write("Welcome to SimpleStart. :smile:")

ss.button("Click Me", type="primary", onclick=myclick)