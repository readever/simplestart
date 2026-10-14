'''
SimpleStart Basics 5/5: charts in a few lines
Run: ss examples/05_chart.py
'''

import simplestart as ss

ss.write("## Charts in Pure Python")

ss.plot.bar(
    data={"A": 10, "B": 15, "C": 13, "D": 20, "E": 18},
    x_label="Category",
    y_label="Value",
    title="Basic Bar Chart",
)

ss.write("That is the whole program - the chart is fully interactive (hover for tooltips).")