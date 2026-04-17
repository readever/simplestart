'''title: Interactive Prediction
order_name: 004 prediction
'''

import simplestart as ss
from sklearn.datasets import load_iris
import numpy as np

#1 Page Text Content

md_content = """

### Interactive Prediction Experiment

This page is used to verify the actual performance of the trained KNN model during the inference phase. By adjusting the input feature parameters, you can observe the classification decisions and confidence changes of the model under different data combinations.

#### Parameter Settings and Prediction

Please adjust the sliders below to input the geometric features of the iris flower (unit: cm). The system will calculate and display the prediction results in real-time based on the values you input.

{slot#slot_slider#This is the slider component slot: containing four sliders for sepal length, sepal width, petal length, and petal width}

---

#### Prediction Results

{slot#slot_result#This is the prediction result display slot: showing the predicted species name and confidence value}

#### Prediction Notes
1. **Parameter Adjustment**: Adjust the sepal and petal dimensions using the sliders, and the system will update the prediction results in real-time.
2. **Model Usage**: The prediction uses the KNN model trained on the Model Training page.
3. **Confidence Calculation**: The confidence is calculated based on the distances of the nearest neighbors in the KNN algorithm. A higher value indicates a more reliable prediction.
4. **Result Interpretation**: The prediction result shows the iris species that the model considers most likely and its confidence level.

"""

row = ss.row(width = "70%")
row.start()

md = ss.md(md_content)

#2 Code Logic
ss.session.warning_str = ""
ss.session.sepal_length = 5.0  # Set reasonable initial values
ss.session.sepal_width = 3.3   # Set reasonable initial values
ss.session.petal_length = 1.4  # Set reasonable initial values
ss.session.petal_width = 0.2   # Set reasonable initial values

# Define iris species names
species_names = ['Setosa', 'Versicolour', 'Virginica']

# Generic feature change handler function
def on_feature_change(event):
    feature_name = event.data["name"]
    
    if feature_name == "petal_width":
        ss.session.petal_width = event.value
    if feature_name == "petal_length":
        ss.session.petal_length = event.value
    if feature_name == "sepal_length":
        ss.session.sepal_length = event.value
    if feature_name == "sepal_width":
        ss.session.sepal_width = event.value

    update_prediction()

def update_prediction():
    if hasattr(ss.store, 'model') and ss.store.model is not None:
        ss.session.warning_str = ""
        # Prepare input data
        input_data = [[
            ss.session.sepal_length,
            ss.session.sepal_width,
            ss.session.petal_length,
            ss.session.petal_width
        ]]
        
        # Prediction
        prediction = ss.store.model.predict(input_data)[0]
        species = species_names[prediction]
        
        # Calculate confidence (using KNN distances as a simple confidence indicator)
        distances, indices = ss.store.model.kneighbors(input_data)
        confidence = 1.0 / (1.0 + np.mean(distances))  # Simple confidence calculation
        
        # Update session variables
        ss.session.prediction = species
        ss.session.confidence = confidence
    else:
        ss.session.warning_str = "Please train the model on the Model Training page first"
        ss.session.prediction = ""
        ss.session.confidence = 0

#ui
# Input parameters
with md.slot("slot_slider"):
    container = ss.container(color = "#fafcff", width = 600, direction = "column")
    container.start()

    # Sepal Length
    ss.text("Sepal Length:")
    ss.slider(value=5.0,min=4.0,max=8.0,step=0.1,onchange=on_feature_change,eventData= {"name":"sepal_length"}, show_input=True, marks={4: '4cm', 8: '8cm'})

    
    ss.space("mb-4")
    
    # Sepal Width
    ss.text("Sepal Width:")
    ss.slider(value=3.3,min=2.0,max=4.5,step=0.1, onchange=on_feature_change,eventData= {"name":"sepal_width"}, show_input=True, marks={2: '2cm', 4.5: '4.5cm'})

    
    ss.space("mb-4")
    
    # Petal Length
    ss.text("Petal Length:")
    ss.slider(value=1.4,min=1.0,max=7.0,step=0.1,onchange=on_feature_change,eventData= {"name":"petal_length"}, show_input=True, marks={1: '1cm', 7: '7cm'})

    
    ss.space("mb-4")
    
    # Petal Width
    ss.text("Petal Width:")
    ss.slider(value=0.2,min=0.1,max=2.5,step=0.1,onchange=on_feature_change,eventData= {"name":"petal_width"}, show_input=True, marks={0.1: '0.1cm', 2.5: '2.5cm'})
    container.end()

with md.slot("slot_result"):
    ss.text(f"Predicted Species: @prediction  Confidence: @confidence")
    ss.text("@warning_str", tag = "mark")

row.end()

update_prediction()
