### Sqlite Database
import simplestart as ss

ss.md("## ss.sqlite Database")

ss.space()
ss.md('''
Provides simple operations for the SQLite database.
''')

ss.space()
ss.md('''
#### 🔅 Example
''')

ss.md('''
::: tip
This example reads the Iris dataset from the SQLite database and displays it in a CSV table format.
For SQLite management, simplestart offers a built-in tool for simple create, read, update, and delete operations.
:::
''')

sql = ss.sqlite("./data/ss_data.db")
df = sql.pd_query("select * from iris")

mytable = ss.table(df, editable = True)###, handlers={"current-change":current_change, "selection-change":selection_change})

ss.space()
ss.write("#### Code")

ss.md('''
```python
import simplestart as ss

sql = ss.sqlite("./data/ss_data.db")
data = sql.pd_query("select * from HousingData")
ss.write(data)
```
''')
