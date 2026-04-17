'''
title: Model Training
order_name: 003 train
'''
# Reference: https://www.kaggle.com/code/nathsubhajit/iris-flower-classification

import simplestart as ss
import time
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# 1. Page Content Markdown Format
# Note: We reserve {slot#xxx#placeholder text} where we need to dynamically display results
md_content = """
### Model Training Laboratory

Before starting predictions, we need to first "teach" the computer how to recognize flowers. This page will demonstrate how to use the **K-Nearest Neighbors (KNN)** algorithm to perform a complete model training process on the Iris dataset.

#### 1. Core Principle: Birds of a Feather Flock Together
The core idea of the KNN algorithm is very intuitive: if a sample in the feature space belongs to the same category as the majority of its **K nearest neighbors**, then that sample also belongs to that category.

We can imagine the distribution of flowers in a coordinate system:
- **Setosa**: Has distinct features, usually clustering in one corner.
- **Versicolor & Virginica**: Have more similar features, and their distribution areas overlap partially.
- **Discrimination Logic**: When we encounter an "unknown flower", we only need to observe the **K nearest neighbors around it**, and the category with the most votes is its identity.

#### 2. Experimental Configuration and Data Splitting
To scientifically evaluate model performance, we follow the standard machine learning workflow - **Hold-out Method**. We randomly split the 150 original samples in a **7:3** ratio:

{slot#config#The parameter configuration table will be displayed here}


::: primary
**💡 About Random State**
The `Random State` here is used to control the randomness of data shuffling. Fixing this value (e.g., 42) ensures that the training and test set split is exactly the same each time, thus guaranteeing the **reproducibility** of experimental results.
:::

#### 3. Execute Training
Click the button below, and the program will automatically execute the following steps:
1.  **Data Loading**: Load the Iris dataset.
2.  **Data Splitting**: Split into training and test sets according to the above configuration.
3.  **Model Construction**: Initialize the KNN classifier (set K=5).
4.  **Model Fitting**: "Learn" features on the training set.
5.  **Model Evaluation**: "Test" on the test set and calculate accuracy.

{slot#train#The training button will be placed here}

---

#### 5. Training Results

{slot#train_result#The model training results will be displayed here...}

---

#### 6. Terminology Explanation and Result Interpretation
- **Accuracy**
    - Definition: The proportion of correctly predicted samples to the total number of samples.
    - Interpretation: The closer to 1.0 (100%), the better the model performs.

- **Confusion Matrix**
    - **Diagonal values**: Represent the number of **correct predictions**. The larger, the better (ideal state is all on the diagonal).
    - **Non-diagonal values**: Represent the number of **incorrect predictions**. For example, the number in the second row, third column represents the number of samples where "Versicolor" was incorrectly classified as "Virginica"<em style="font-size: small">(test result with random seed of 5)</em>. The smaller, the better.
"""

row = ss.row(width="70%")
row.start()

# Render Markdown
md = ss.markdown(md_content)

#2 Code Logic

# Define hyperparameters
TEST_SIZE = 0.3
RANDOM_STATE = 42
K_NEIGHBORS = 5

# Construct DataFrame for configuration table
config_data = {
    'Parameter Name': ['Algorithm Model', 'K Value (Number of Neighbors)', 'Train/Test Ratio', 'Random State', 'Distance Metric'],
    'Set Value': ['KNN (K-Nearest Neighbors)', K_NEIGHBORS, '70% / 30%', "@random_state", 'Minkowski (p=2)'],
    'Description': ['Distance-based classification algorithm', 'Number of neighbors that determine the voting range', '105 samples for training, 45 samples for testing', 'Fix data splitting method to ensure reproducibility', 'i.e., Euclidean distance, calculating straight-line distance']
}

### -----------------------


cm_table = None
ss.session.acc = ""

# Define training logic
def run_training():
    global cm_table
    #with ss.spinner("Model is being trained, please wait..."):
    time.sleep(1.5)  # Simulate time-consuming operation
    
    # --- Real machine learning code ---
    iris = load_iris()
    RANDOM_STATE = ss.session.random_state
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=TEST_SIZE, random_state=RANDOM_STATE)

    
    knn = KNeighborsClassifier(n_neighbors=K_NEIGHBORS)
    #Start training the model
    knn.fit(X_train, y_train)
    
    # Save the trained model to Session State for use elsewhere
    ss.store.model = knn
    
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(f"accuracy: {acc:.4f}")
    # -----------------------
    
    # Save results to Session State for use elsewhere
    ss.store.model = knn
    ss.session.acc = f"{acc:.4f}"
    ss.store.cm = cm
    ss.store.model_trained = True
    
    # Update training result display
    cm_df = pd.DataFrame(cm, index=['Setosa', 'Versicolour', 'Virginica'], 
                        columns=['Setosa', 'Versicolour', 'Virginica'])

    # Update confusion matrix table data
    cm_table.prop.tableData = cm_df



# config slot -- Display configuration table
config_df = pd.DataFrame(config_data)
with md.slot("config"):
    ss.table(config_df, width="80%", border=True)


# train slot -- Display training button
with md.slot("train"):
    ss.button("Train Model", type="primary", onclick=run_training)


# train_result slot -- Display training result
with md.slot("train_result"):
    ss.write("**Accuracy**: @acc")

    ss.write("**Confusion Matrix**:")

    # Display confusion matrix
    cm_table = ss.table(pd.DataFrame(), width=400, border=True)

row.end()


#Sidebar
import random
ss.session.random_state = 5
def shuffle_random():
    ss.session.random_state = random.randint(1, 1000)

def reset_random_state():
    ss.session.random_state = 5

with ss.sidebar():
    ss.write("Current Random Seed: @random_state")
    ss.button("Update Random Seed", onclick=shuffle_random)
    ss.space("mb-4")
    ss.button("Reset Random Seed", onclick=reset_random_state)