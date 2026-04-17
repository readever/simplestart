'''title: Project Introduction
order_name: 001 introduction
'''

import simplestart as ss

# Content layout for data exploration page

md_content = """
### Iris Classification Project

Welcome to the Iris Dataset Exploration and Classification Application. This is a classic beginner project in machine learning, designed to help users understand data features and predict iris species through an interactive interface.

---

#### Dataset Introduction
The Iris dataset was organized and published by British statistician Ronald Fisher in 1936, and is regarded as the **"Hello World"** of machine learning. It contains 150 samples, divided into 3 different iris species, with 50 samples each:

1.  **Setosa**: Shorter but wider sepals, with the strongest linear separability.
2.  **Versicolor**: Features intermediate between the other two.
3.  **Virginica**: Typically has larger petals and sepals.

{slot#iris_gallery#Comparison images of the three iris species will be displayed here}

#### Feature Description
Each sample contains 4 key morphological features that we will use for modeling:

| Feature Name | English Key | Description |
| :--- | :--- | :--- |
| **Sepal Length** | `sepal length` | External length of the sepal (cm) |
| **Sepal Width** | `sepal width` | External width of the sepal (cm) |
| **Petal Length** | `petal length` | Length of the petal (cm) |
| **Petal Width** | `petal width` | Width of the petal (cm) |

---

#### Application Objectives
This application aims to guide you through the data analysis process in three steps:
1.  **Data Exploration**: Visualize and analyze the distribution differences of different species in sepal and petal dimensions.
2.  **Model Training**: Build a classification model using the **K-Nearest Neighbors (KNN)** algorithm.
3.  **Interactive Prediction**: Build a real-time interface where you can input dimensions to predict the species.

"""

row = ss.row(width = "70%")  
row.start()

md = ss.markdown(md_content)

# Code Logic
with md.slot("iris_gallery"):
    ss.image(
        src="./data/iris.png",
        width="100%",
        alt="Iris Dataset"
    )

    with ss.row(justify="center"):
        ss.text("Iris Legend, Source: ", tag = "b", color = "gray")
        ss.link("Kaggle Learn", href = "https://storage.googleapis.com/kaggle-media/learn/images/RcxYYBA.png", type = "warning")

row.end()