### ss.template

import simplestart as ss

ss.md("## ss.template Load VUE Template")

ss.space("mt-8")
ss.md('''
In SimpleStart, you can define simple Vue components using ss.template to achieve property and data interaction.

#### Function
ss.template(src, path, data, handlers)

##### Function Description

| Parameter | Description |
| --- | --- | 
| src | Component script in string format |
| path | Path to the original code of the external component file |
| data | Data used for interaction between frontend components and the Python backend |
| handlers | Events defined in the frontend component, implemented on the Python side |
      
''')

ss.space("mt-8")

    
template = '''
  <v-card
    class="mx-auto text-white"
    color="#26c6da"
    max-width="400"
    prepend-icon="mdi-twitter"
    title="Twitter"
  >
    <template v-slot:prepend>
      <v-icon size="x-large"></v-icon>
    </template>

    <v-card-text class="text-h6 py-2">
      "SimpleStart is a easy way to build webpage and visualize data."
    </v-card-text>

    <v-card-actions>
      <v-list-item class="w-100">
        <template v-slot:prepend>
          <v-avatar
            color="grey-darken-3"
            image="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
          ></v-avatar>
        </template>

        <v-list-item-title>Evan You</v-list-item-title>

        <v-list-item-subtitle>Data Science Engineer</v-list-item-subtitle>

        <template v-slot:append>
          <div class="justify-self-end">
            <v-icon class="me-1" icon="mdi-heart" \@click="onserver('myclick')"></v-icon>
            <span class="subheading me-2">{{data.vote}}</span>
            <span class="me-1">·</span>
            <v-icon class="me-1" icon="mdi-share-variant"></v-icon>
            <span class="subheading">45</span>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
'''

def myclick(event):
    mycard.vote  = mycard.vote + 1
    
data = {"vote":256}
mycard = ss.template(template, data = data, handlers = {"myclick":myclick})

def increment(event):
    mycard.vote  = mycard.vote + 1
    #mycard.style = "color:red"

ss.space()
ss.button("Thumb Up", onclick=increment)

ss.space("mt-8")

ss.write('''
---
#### Python Side Code
''')

ss.md('''
```python
import simplestart as ss

template = \'''
  <v-card
    class="mx-auto text-white"
    color="#26c6da"
    max-width="400"
    prepend-icon="mdi-twitter"
    title="Twitter"
  >
    <template v-slot:prepend>
      <v-icon size="x-large"></v-icon>
    </template>

    <v-card-text class="text-h6 py-2">
      "SimpleStart is a easy way to build webpage and visualize data."
    </v-card-text>

    <v-card-actions>
      <v-list-item class="w-100">
        <template v-slot:prepend>
          <v-avatar
            color="grey-darken-3"
            image="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
          ></v-avatar>
        </template>

        <v-list-item-title>Evan You</v-list-item-title>

        <v-list-item-subtitle>Data Science Engineer</v-list-item-subtitle>

        <template v-slot:append>
          <div class="justify-self-end">
            <v-icon class="me-1" icon="mdi-heart" \@click="onserver('myclick')"></v-icon>
            <span class="subheading me-2">{{data.vote}}</span>
            <span class="me-1">·</span>
            <v-icon class="me-1" icon="mdi-share-variant"></v-icon>
            <span class="subheading">45</span>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
\'''

def myclick(event):
    mycard.vote  = mycard.vote + 1
    
data = {"vote":256}
mycard = ss.template(template, data = data, handlers = {"myclick":myclick})

def increment(event):
    mycard.vote  = mycard.vote + 1
    #mycard.style = "color:red"

ss.space()
ss.button("Thumb Up", onclick=increment)
```
''')


ss.space("mt-8")

def onPageEnter():
    ss.session["counter"] = 0
    