import streamsync as ss

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


#下载不了，所以加一个参数data_home
data_home = "./data/seaborn"

ss.md('''
## ss.pyplot Drawing
''')


ss.space()
ss.md('''
#### 🔅 Example
''')

ss.write("#### 1. Draw a Line Plot")

sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic", data_home=data_home)
sns.lineplot(x="age", y="fare", hue="sex", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")

ss.write("#### 2. Draw a Scatter Plot")

sns.set_style("whitegrid")
tips = sns.load_dataset("tips", data_home=data_home)
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")

ss.write("#### 3. Draw a Bar Plot")

sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic",data_home=data_home)
sns.barplot(x="class", y="survived", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")


ss.write("#### 4. Draw a Histogram")
sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic",data_home=data_home)
sns.histplot(x="age", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")


ss.space()

ss.write("#### 🔎 Code")
ss.write("---")

def viewcode():
    ss.session["viewcode"] = 1

ss.button("View Code", size="small", onclick = viewcode)


def conditioner(event):
    return ss.session["viewcode"] == 1

with ss.when(conditioner):
    ss.md('''
```python
import streamsync as ss

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


data_home = "./data/seaborn"


ss.write("#### 1. Draw a Line Plot")

sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic", data_home=data_home)
sns.lineplot(x="age", y="fare", hue="sex", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")

ss.write("#### 2. Draw a Scatter Plot")

sns.set_style("whitegrid")
tips = sns.load_dataset("tips", data_home=data_home)
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")

ss.write("#### 3. Draw a Bar Plot")

sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic",data_home=data_home)
sns.barplot(x="class", y="survived", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")


ss.write("#### 4. Draw a Histogram")
sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic",data_home=data_home)
sns.histplot(x="age", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")
```
    ''')
    
