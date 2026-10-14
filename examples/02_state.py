'''
SimpleStart Basics 2/5: reactive session state (ss.session)
Run: ss examples/02_state.py
'''

import simplestart as ss

ss.session.name = "world"

ss.write("## Reactive Session")
ss.write("Change the text below - the page updates instantly, no reload.")

def change_name(event):
    ss.session.name = event.value

ss.text_input("world", onchange=change_name)

ss.write("Hello, @@name!")