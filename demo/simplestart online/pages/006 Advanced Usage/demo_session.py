### ss.session
import simplestart as ss

ss.md("## ss.session Session Variables")

ss.space()


#in this page
ss.session["count"] = 100

mytext = ss.text("The couns is @count")


def change_count():
    ss.session.count += 1

ss.button("Add Count", onclick=change_count)

def onPageEnter():
    ss.session.count = 100