### Introduction
import simplestart as ss

ss.md('''
## Iris Dataset
The Iris dataset is a commonly used classification dataset, compiled by Fisher in 1936. Also known as the Iris flower dataset, it is a multivariate analysis dataset. The dataset contains 150 samples divided into 3 classes, with 50 samples each, and each sample has 4 attributes. The attributes—sepal length, sepal width, petal length, and petal width—can be used to predict which of the three species (Setosa, Versicolor, Virginica) an Iris flower belongs to.

### Iris Flower
Iris flowers have a rich cultural background. They are named for their petals, which resemble the tails of birds. The Latin genus name "iris" means "rainbow" in Greek, symbolizing the variety of flower colors.
''')


with ss.row(style="margin:10px 0"):
    with ss.col():
        ss.image("./images/setosa.webp", title = "Silky Iris Setosa", elevation = 10, width=250)

    with ss.col():
        ss.image("./images/versicolor.webp", title = "Iris Versicolor", elevation = 10, width=250)

    with ss.col():
        ss.image("./images/virginica.webp", title = "Virginia Iris Virginica", elevation = 10, width=250)

ss.md('''
### Machine Learning

This tutorial will use the scikit-learn library to build a machine learning classification model to predict the species of Iris flowers. Specifically, we will train and test the model using measurement data from the Iris flowers—including petal and sepal lengths and widths. Our goal is to teach the model how to learn from these labeled data through the application of several classic machine learning algorithms, enabling accurate species predictions for new Iris flowers.

''')

ss.md('''
###
References for this example include:
---
[1. Basic Machine Learning: 1.7 Iris Classification](https://blog.csdn.net/qq_47809408/article/details/124632290)
[2. Introduction to KNN Classification Algorithm: Classifying the Iris Dataset](https://blog.csdn.net/weixin_51756038/article/details/130096706)
[3. Interactive Web App with Streamlit and Scikit-learn](https://github.com/patrickloeber/streamlit-demo)
''')
