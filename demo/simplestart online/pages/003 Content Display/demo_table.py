### Table
import simplestart as ss
import pandas as pd

ss.md("## ss.table Table Data")

ss.md("Display data in table format.")

ss.space()

ss.md('''
#### 🔅 Example
''') 

def onchange_index(event):
    value = event.value

    if value == True:
        ss.getcm().components[mytable.id]["content"]["index"] = True
        ss.session["showIndex"] = ', index = True'
    else:
        ss.getcm().components[mytable.id]["content"]["index"] = False
        ss.session["showIndex"] = ''
    mytable.update()
    
def onchange_border(event):
    value = event.value

    if value == True:
        ss.getcm().components[mytable.id]["content"]["border"] = True
        ss.session["showBorder"] = ', border = True'
    else:
        ss.getcm().components[mytable.id]["content"]["border"] = False
        ss.session["showBorder"] = ''
    mytable.update()


def onchange_sortable(event):
    value = event.value

    if value == True:
        ss.getcm().components[mytable.id]["content"]["sortable"] = True
        ss.session["sortable"] = ', sortable = True'
    else:
        ss.getcm().components[mytable.id]["content"]["sortable"] = False
        ss.session["sortable"] = ''
    mytable.update()
    
def onchange_searchable(event):
    value = event.value

    if value == True:
        ss.getcm().components[mytable.id]["content"]["searchable"] = True
        ss.session["searchable"] = ', searchable = True'
    else:
        ss.getcm().components[mytable.id]["content"]["searchable"] = False
        ss.session["searchable"] = ''
    mytable.update()


def onchange_selectable(event):
    value = event.value

    if value == True:
        ss.getcm().components[mytable.id]["content"]["selectable"] = True
        ss.session["selectable"] = ', selectable = True'
    else:
        ss.getcm().components[mytable.id]["content"]["selectable"] = False
        ss.session["selectable"] = ''  
    mytable.update()
    
def onchange_editable(event):
    value = event.value

    if value == True:
        ss.getcm().components[mytable.id]["content"]["editable"] = True
        ss.session["editable"] = ', editable = True'
    else:
        ss.getcm().components[mytable.id]["content"]["editable"] = False
        ss.session["editable"] = ''  
    mytable.update()

     
def current_change(state, value):
    ss.session["row_selected"] = value["index"]
    
def selection_change(state, value):
    ss.session["selection_change"] = value["selected"]
        
        
# Create a dataset with three columns
data = {'name': ['👧🏻 Alice', '👦🏻 Bob', '👦🏻 Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'Los Angeles'],
        'health':[90,80,90]
       }

df = pd.DataFrame(data)

def rowclicked(event):
    #ss.message("row clicked")
    #ss.write("event", event)
    ss.session["itemname"] = event.value["name"]
    

cols = ss.columns([70,"flex:30; border-left:1px solid lightgray"], design=True, style="border:1px solid lightgray")
with cols[0]:
    mytable = ss.table(df, handlers={"click:row": rowclicked})
    ss.md("#### Events")
    ss.write("Row clicked: @itemname")


with cols[1]:
    ss.text("setting")    
    ss.checkbox("Index", onchange = onchange_index) 
    ss.space()
    ss.checkbox("Border", onchange = onchange_border) 
    ss.space()
    ss.checkbox("Sort", onchange = onchange_sortable)
    ss.space()
    ss.checkbox("Select", onchange = onchange_selectable)
    ss.space()
    ss.checkbox("Search", onchange = onchange_searchable)
    ss.space()
    ss.checkbox("Edit", onchange = onchange_editable)
    
ss.space("mt-8")

ss.write('''
---
#### 🔎 Code
''')

ss.md('''
```python
import simplestart as ss

def current_change(state, value):
    ss.session["row_selected"] = value["index"]
    
def selection_change(state, value):
    ss.session["selection_change"] = value["selected"]

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

ss.table(df, handlers={\"current-change\":current_change, \"selection-change\":selection_change})
ss.md(\"#### Events\")
ss.write(\"Row selected: \")
ss.write(\"Selection changed: \")
    
def onPageLoad():
    ss.session["row_selected"] = ''
    ss.session["selection_change"] = ''
    
```
''')


ss.md('''
---
#### 🔅 Example - Custom column.
''')


data = {'name': ['👧🏻 Alice', '👦🏻 Bob', '👦🏻 Charlie'],
        'age': [25, 30, 35],
        'city': [':sunny: New York', ':cloud: San Francisco', ':sunny: Los Angeles'],
        'health':[90,80,90]
       }

df = pd.DataFrame(data)

cols = ss.columns([70,"flex:30; border-left:1px solid lightgray"], design=True, style="border:1px solid lightgray")


vuecode = '''
<template>
<v-clip>123</v-clip>
</template>
'''

vuecode = "../components/mycell.vue"

#mytable_ex = ss.table(df, custom_columns = ["city"], custom_columns_template = vuestr)
with cols[0]:
    mytable_ex = ss.table(df, custom_columns = ["city"], vue_columns = ["health"], vue_code = vuecode)
with cols[1]:
    ss.write("Each column can be customized for display.")
    
ss.space("mt-8")

ss.write('''
---
#### 🔎 代码
''')

ss.md('''
```python
import simplestart as ss

data = {'name': ['👧🏻 Alice', '👦🏻 Bob', '👦🏻 Charlie'],
        'age': [25, 30, 35],
        'city': [':sunny: New York', ':cloud: San Francisco', ':sunny: Los Angeles'],
        'health':[90,80,90]
        }
df = pd.DataFrame(data)

vuestr = \'''
<template>
    <v-row>
    <v-rating
      v-model="rating" density="compact" color="orange" half-increments></v-rating>
    <v-chip variant="text">{{item.value}}</v-chip>
        </v-row>
</template>

<script>

module.exports = {
    props:["item"],
    
    data () {
        return {
            rating: 3
        }
    },
    methods: {
        //todo
    },
    mounted: function () {
        this.rating = this.item.value/20
    },
}
</script>
\'''

ss.table(df, custom_columns = ["city"], vue_columns = ["health"], vue_code = vuecode)
```
''')

def onPageLoad():
    ss.session["show_border"] = ''
    ss.session["selectable"] = ''
    ss.session["sortable"] = ''
    ss.session["row_selected"] = ''
    ss.session["selection_change"] = ''