### Prediction Instance
# The original source code:
# https://github.com/AzeemWaqarRao/Streamlit-Iris-Classification-App
import simplestart as ss

from sklearn.datasets import load_iris
import pandas as pd
import pickle
import numpy as np

# Data and API
species = ['setosa', 'versicolor', 'virginica']
image = ['./images/setosa.jpg', './images/versicolor.jpg', './images/virginica.jpg']
with open('./data/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
def slidechange(event):
    predict()

def predict():
    # Getting prediction from model
    inp = np.array([sepal_length.value, sepal_width.value, petal_length.value, petal_width.value])
    inp = np.expand_dims(inp, axis=0)
    prediction = model.predict_proba(inp)

    ## Show results when prediction is done
    if True:
        df = pd.DataFrame(prediction, index=['result'], columns=species).round(4)
        table_result.data = df
        ss.session["result"] = species[np.argmax(prediction)]
        image_flower.image = image[np.argmax(prediction)]
        
# UI 
with ss.sidebar():
    ss.write("### Inputs")
    
    sepal_length = ss.slider("sepal length (cm)", 4.3, 7.9, 5.0, onchange=slidechange)
    sepal_width = ss.slider("sepal width (cm)", 2.0, 4.4, 3.6, onchange=slidechange)
    petal_length = ss.slider("petal length (cm)", 1.0, 6.9, 1.4, onchange=slidechange)
    petal_width = ss.slider("petal width (cm)", 0.1, 2.5, 0.2, onchange=slidechange)

ss.write("## Iris Flower Classification Prediction")
ss.write("Change the sepal and petal length and width to predict among the 3 possible categories.")

ss.write('''
# Results
Following is the probability of each class
''')

ss.space()

table_result = ss.table(show_border=True)
ss.write("**This flower belongs to the @result" + " class**")

ss.space()

image_flower = ss.image(image[0])
    
predict()
