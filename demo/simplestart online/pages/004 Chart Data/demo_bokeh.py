import simplestart as ss

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.resources import CDN
from bokeh.embed import file_html
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})


# Create the data source and figure object
source = ColumnDataSource(data=dict(
    sepal_length=df['sepal length (cm)'],
    sepal_width=df['sepal width (cm)'],
    petal_length=df['petal length (cm)'],
    petal_width=df['petal width (cm)'],
    species=df['species']
))

# Create a Bokeh scatter plot
p = figure(title="Iris Dataset Scatter Plot", x_axis_label='Sepal Length (cm)', y_axis_label='Sepal Width (cm)',
           tools="pan,wheel_zoom,box_zoom,reset,hover,save", width=800)

# Set different colors based on species
colors = {'setosa': 'blue', 'versicolor': 'green', 'virginica': 'red'}

for species, color in colors.items():
    df_species = df[df['species'] == species]
    source_species = ColumnDataSource(data=dict(
        sepal_length=df_species['sepal length (cm)'],
        sepal_width=df_species['sepal width (cm)']
    ))
    p.scatter('sepal_length', 'sepal_width', source=source_species, legend_label=species, color=color,
              size=10, alpha=0.5)

p.legend.title = 'Species'
p.legend.location = 'top_left'

# Embed the Bokeh figure into SimpleStart
html = file_html(p, CDN, "Iris Dataset Scatter Plot")

#ui
ss.md('''
## simplestart Chart Demo - Bokeh
''')

ss.space()
ss.md('''
#### 🔅 Example
An interactive scatter plot of the Iris data using Bokeh
''')

ss.space()
ss.htmlview(html, border = False)

ss.space()
ss.write("#### 🔎 Code")

def viewcode():
    ss.session["viewcode"] = 1

ss.session["viewcode"] = 0
ss.button("View Code", size="small", onclick = viewcode)

def conditioner(event):
    return (ss.session["viewcode"] == 1)

code = '''
```python
import simplestart as ss

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.resources import CDN
from bokeh.embed import file_html
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})


# Create the data source and figure object
source = ColumnDataSource(data=dict(
    sepal_length=df['sepal length (cm)'],
    sepal_width=df['sepal width (cm)'],
    petal_length=df['petal length (cm)'],
    petal_width=df['petal width (cm)'],
    species=df['species']
))

# Create a Bokeh scatter plot
p = figure(title="Iris Dataset Scatter Plot", x_axis_label='Sepal Length (cm)', y_axis_label='Sepal Width (cm)',
           tools="pan,wheel_zoom,box_zoom,reset,hover,save", width=800)

# Set different colors based on species
colors = {'setosa': 'blue', 'versicolor': 'green', 'virginica': 'red'}

for species, color in colors.items():
    df_species = df[df['species'] == species]
    source_species = ColumnDataSource(data=dict(
        sepal_length=df_species['sepal length (cm)'],
        sepal_width=df_species['sepal width (cm)']
    ))
    p.scatter('sepal_length', 'sepal_width', source=source_species, legend_label=species, color=color,
              size=10, alpha=0.5)

p.legend.title = 'Species'
p.legend.location = 'top_left'

# Embed the Bokeh figure into SimpleStart
html = file_html(p, CDN, "Iris Dataset Scatter Plot")

#ui
ss.htmlview(html, border = False)
'''

with ss.when(conditioner):
    ss.md(code)