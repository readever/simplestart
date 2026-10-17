'''
SimpleStart Basics 4/5: display data with table and card
Run: ss examples/04_data.py
'''

import simplestart as ss

ss.write("## Sales Dashboard Sample")

mydata = [
    {"Month": "Jan", "Sales": 120, "Profit": 30},
    {"Month": "Feb", "Sales": 200, "Profit": 60},
    {"Month": "Mar", "Sales": 150, "Profit": 45},
]

with ss.card(style="max-width:520px"):
    ss.table(tableData=mydata, stripe=True)

ss.space()

with ss.card(style="max-width:520px"):
    ss.write("### Monthly Report")
    ss.text("March profit margin: <b>30%</b> - a record high. 📈", type="success")