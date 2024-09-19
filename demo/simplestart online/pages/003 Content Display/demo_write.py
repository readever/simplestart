### Write

import streamsync as ss
import pandas as pd

ss.md("## ss.write Output Data")

ss.md("ss.write is similar to print; it can output text, lists, and other types, making testing and output easy.")

ss.space()

ss.md('''
#### 🔅 Example
''')


ss.md("#### 1. Output Text")
ss.write("This is a text")

ss.md('''
```python
ss.write("This is a text")
```
''')

ss.md("#### 2. Output Multiple Variables")
a = "aaa"
b = "bbb"
ss.write(a, ",", b)

ss.md('''
```python
a = "aaa"
b = "bbb"
ss.write(a, ",", b)
```
''')

ss.md("#### 3. Output List")
data = ["aaa", "bbb", "ccc"]
ss.write(data)

data = {"aaa":1, "bbb":2, "ccc":3}
ss.write(data)

ss.md('''
```python
data = ["aaa", "bbb", "ccc"]
ss.write(data)

data = {"aaa":1, "bbb":2, "ccc":3}
ss.write(data)
```
''')


ss.md("#### 4. Output Table")
# 创建数据
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Paris', 'London', 'Sydney']}

# Convert data to DataFrame format
df = pd.DataFrame(data)
ss.write(df)

ss.md('''
```python
# Create data
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Paris', 'London', 'Sydney']}

# Convert data to DataFrame format
df = pd.DataFrame(data)
ss.write(df)
```
''')