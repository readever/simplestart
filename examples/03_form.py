'''
SimpleStart Basics 3/5: build a form with input widgets
Run: ss examples/03_form.py
'''

import simplestart as ss

ss.write("## Coffee Order Form")

def place_order():
    ss.message("Order placed! ☕", type = "success")

with ss.card(style="max-width:520px"):
    ss.write("**Your name**")
    ss.text_input(value="", placeholder="Type your name...")

    ss.write("**Size**")
    ss.selectbox(options=["Small", "Medium", "Large"], value="Medium")

    ss.write("**Sugar (spoons)**")
    with ss.panel(width=420, border=False):
        ss.slider(value=1, min=0, max=5)

    ss.space("mt-4")
    ss.button("Place Order", type="primary", onclick=place_order)