'''
SimpleStart Basics 3/5: build a form with input widgets
Run: ss examples/03_form.py
'''

import simplestart as ss

ss.write("## Coffee Order Form")

ss.session.name = ""
ss.session.size = "Medium"
ss.session.sugar = 1
ss.session.order = ""

def set_name(event):  ss.session.name = event.value
def set_size(event):  ss.session.size = event.value
def set_sugar(event): ss.session.sugar = event.value

def place_order():
    name = ss.session.name or "Guest"
    ss.session.order = f"One {ss.session.size} coffee with {ss.session.sugar} sugar(s) for {name}. ☕"

with ss.card(style="max-width:520px"):
    ss.write("**Your name**")
    ss.text_input(value="", placeholder="Type your name...", onchange=set_name)

    ss.write("**Size**")
    ss.selectbox(options=["Small", "Medium", "Large"], value="Medium", onchange=set_size)

    ss.write("**Sugar (spoons)**")
    ss.slider(value=1, min=0, max=5, onchange=set_sugar)

    ss.space("mt-4")
    ss.button("Place Order", type="primary", onclick=place_order)
    ss.write("@@order")