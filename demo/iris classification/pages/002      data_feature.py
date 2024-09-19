### Feature Analysis

import simplestart as ss
import pandas as pd

ss.md('''
## Feature Analysis
''')

ss.space()

ss.md("#### 1. Scatter Matrix of Features")
ss.space()
ss.image("./images/feature01.png", width=600, height=500)

ss.space()

ss.md('''
This image is from:
[VuNus 【Basics of Machine Learning】1.7 Iris Flower Classification](https://blog.csdn.net/qq_47809408/article/details/124632290)
''')

ss.space()
ss.md("#### 2. Feature Exploration")
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.embed import file_html
from bokeh.resources import CDN
from bokeh.palettes import Category10

# Load dataset
data = pd.read_csv("./data/iris.csv")

# Create Bokeh chart
p = figure(title="Iris Dataset Scatter Plot", x_axis_label='Petal Length (cm)', y_axis_label='Petal Width (cm)',
           tools="pan,wheel_zoom,box_zoom,reset,hover,save", width=800, height=600)

# Create data source
source = ColumnDataSource(data)

# Set color mapping for species column
species_list = data['species'].unique().tolist()
p.circle(x='petal_length', y='petal_width', source=source, size=10,
         color=factor_cmap('species', palette=Category10[3], factors=species_list), legend_field='species')

# Configure legend
p.legend.title = "Species"
p.legend.location = "top_left"

# Convert Bokeh chart to HTML and display
html_output = file_html(p, CDN, "Iris Dataset Scatter Plot")
# show(p)

ss.htmlview(html_output)
