### Data Exploration
import simplestart as ss
import pandas as pd

ss.md('''
## Iris Dataset
The dataset contains 150 samples divided into 3 classes: Setosa, Versicolor, and Virginica. Each class has 50 samples, and each sample includes 4 attributes.
''')

ss.space()

title = "Table 1. Iris Dataset"
subtitle = "sepal_length: length of the sepal, sepal_width: width of the sepal, petal_length: length of the petal, petal_width: width of the petal"
# Set global float display precision
pd.options.display.float_format = '{:.2f}'.format
df = pd.read_csv("./data/iris.csv")

ss.table(df, index=True, title=title, subtitle=subtitle, width=400)

ss.table(df.describe(), index=True)

ss.md("---")
# Simulated Data
import numpy as np
# Set random seed for reproducibility
np.random.seed(0)

num_rows = 10000
data = {
    'Column1': np.random.randint(0, 100, size=num_rows),  # Random integers
    'Column2': np.random.random(size=num_rows),            # Random floats
    'Column3': np.random.choice(['A', 'B', 'C', 'D'], size=num_rows),  # Randomly chosen categories
}
