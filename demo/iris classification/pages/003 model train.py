### Model Training

import simplestart as ss

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


ss.md('''
## Model Training
''')

# Load data and split samples
data = datasets.load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Page session variables
ss.session["acc"] = ""
ss.session["code"] = 0

# Training function
def train(event):
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    acc = round(acc, 2)
    
    ss.session["acc"] = acc  # Assign the result to page session variable, the corresponding page display will respond automatically

ss.md('''
#### Main Steps of Model Training:
First, the Iris dataset is loaded (including features and labels), and this data is split into training and testing sets, with 80% used for training and 20% for testing. Then, a training function is defined that uses the K-Nearest Neighbors (KNN) classifier to train the model, evaluate the predictive accuracy, and save the result in a page session variable for display on the webpage.
###
On the webpage, there is a training button. When the user clicks this button, the training function is triggered, the model is trained in the background, and the predictive accuracy on the test set is calculated. Once training is complete, the accuracy result is updated on the page and displayed to the user in the format "Accuracy = @acc," where @acc is the predictive accuracy value calculated during training.
###
The speed of training and testing is particularly fast because the Iris dataset is very small, containing only 150 samples and 4 features. Additionally, K-Nearest Neighbors (KNN) is a simple and efficient algorithm, especially effective on small datasets, thus the training and testing processes are completed quickly.
###
---
''')
ss.write(f'Test set predictive accuracy Accuracy =', "@acc")

ss.button("Train", onclick=train)
# UI

ss.md("---")

def conditioner(event):
    return ss.session["code"] == 1

def checkcode(event):
    ss.session["code"] = 1
    
def hidecode(event):
    ss.session["code"] = 0

ss.button("View Code", onclick=checkcode)
ss.button("Hide Code", onclick=hidecode)

with ss.when(conditioner):
    ss.md('''
```python
import simplestart as ss

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data and split samples
data = datasets.load_iris()
X = data.data
y = data.target
ss.write(X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Page session variable
ss.session["acc"] = ""

# Training function 
def train(event):
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    acc = round(acc, 2)

    ss.session["acc"] = acc  # Assign the result to page session variable, the corresponding page display will respond automatically

# Display the model's accuracy on the test set
ss.write(f'Test set predictive accuracy Accuracy =', "\@acc")

ss.button("Train", onclick=train)

```
    ''')


ss.md("---")


ss.md('''
::: tip
  ### Advantages of KNN:
  Simple, easy to understand, easy to implement, requires no parameter estimation, no training required;
  Suitable for classifying rare events;
  Particularly suitable for multi-class problems (Multi-label, objects with multiple category labels).
:::
''')

ss.md('''
For more information on KNN, please refer to
[KNN Classification Algorithm Introduction, Classifying Iris Dataset with KNN（iris）](https://blog.csdn.net/weixin_51756038/article/details/130096706)
''')