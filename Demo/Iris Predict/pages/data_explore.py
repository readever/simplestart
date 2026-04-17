'''title: Data Exploration
order_name: 002 data_exploration
'''

import simplestart as ss
from sklearn.datasets import load_iris
import pandas as pd

# Content layout for data exploration page
md_content = """
### Iris Dataset Exploration and Analysis

#### 1. Data Overview
This is a classic classification dataset in machine learning, containing 50 samples each of 3 different species of iris flowers, totaling 150 samples.
Let's first look at the first few rows of the original data:

{slot#data_table#The first 20 rows of data will be displayed here}

---

#### 2. Feature Distribution Visualization: Sepal Length vs Width
To intuitively understand the morphological differences between different species, we selected **sepal length** and **sepal width** for scatter plot analysis.

Please observe the scatter plot below:

{slot#scatter_plot#The scatter plot showing the sepal length and width relationships of different species will be displayed here.}

::: primary
**💡 Interpretation**
**Blue dots (Setosa)**: Clustered in the upper left, indicating that setosa irises typically have shorter but wider sepals, making them relatively easy to distinguish from the other two classes.
**Orange dots (Versicolor) & Green dots (Virginica)**: Mainly distributed on the lower right side, and there is some overlap between their distributions.
:::

---

#### 3. Statistical Feature Analysis
In addition to visualization, we have also calculated statistical summaries of the numerical features. The table below shows the mean, standard deviation, minimum, and maximum values of each feature.

{slot#describe_table#The statistical summary of numerical features will be displayed here.}

---

#### 4. Conclusion
Through this exploration, we can find that the **Setosa** species performs best in linear separability, as it can be easily distinguished from the other two classes based on sepal length and width alone. For **Versicolor** and **Virginica**, it may be necessary to introduce petal-related features to achieve better classification results.

"""

row = ss.row(width = "70%")  
row.start()

md = ss.markdown(md_content)


# Code Logic

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})


# Display data table (first 20 rows)
with md.slot("data_table"):
    # Using simplestart table component or displaying pandas style
    ss.table(tableData=df.head(20), width = 800, height = 250, stripe=True)

# Display scatter plot (sepal length vs width)
with md.slot("scatter_plot"):
    # Using simplestart scatter plot component
 
    # Prepare scatter plot data
    x_data = df['sepal length (cm)'].tolist()
    y_data = df['sepal width (cm)'].tolist()
    hue_data = df['species'].tolist()

    # Draw scatter plot (using hue_data parameter)
    ss.plot.scatter(
        x=x_data,
        y=y_data,
        title="Iris Scatter Plot",
        x_label="Sepal Length (cm)",
        y_label="Sepal Width (cm)",
        hue_data=hue_data,
        width="700px",
        height="500px"
    )
    
# Display statistical feature analysis table
with md.slot("describe_table"):
    # Calculate statistical summary and add median column
    describe_df = df.describe()
    # Round numerical values to 2 decimal places
    describe_df = describe_df.round(2)

    # Convert index to column for table display
    describe_df_reset = describe_df.reset_index()
    # Rename index column
    describe_df_reset = describe_df_reset.rename(columns={'index': 'Statistic'})
    
    # Prepare column configuration
    columns = [{'prop': 'Statistic', 'label': 'Statistic'}]
    for col in describe_df_reset.columns[1:]:
        columns.append({'prop': col, 'label': col})
    
    # Convert to table data format
    table_data = describe_df_reset.to_dict('records')
    
    # Using simplestart table component
    ss.table(tableData=table_data, columns=columns, width=800, stripe=True)

row.end()