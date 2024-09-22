import simplestart as ss
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.resources import CDN
from bokeh.embed import file_html, components

### ui
ss.write('# Bernoulli Distribution Visualization')


def plot(p=0.5):
    x = [0, 1]
    y = [1 - p, p]

    colors = ['#1f77b4', '#ff7f0e']
    source = ColumnDataSource(data=dict(x=x, y=y, color=colors))
    source.name = "mysource"

    fig = figure(
        title="Bernoulli Distribution",
        x_axis_label="Outcome",
        y_axis_label="Probability",
    )

    fig.title.align = "center"

    fig.vbar(x="x", top="y", width=0.5, color="color", source=source)

    return file_html(fig, CDN, "Bernoulli Distribution")

ss.htmlview(plot())

def change_value(value):
    js = f'''
        const iframe = document.getElementById('myIframe');

        const innerWindow = iframe.contentWindow;

        const bokehDoc = iframe.contentWindow.Bokeh.documents[0];
        const source = bokehDoc.get_model_by_name("mysource"); 
        //console.log("source", source)

        // updata source data
        var value = {value};
        source.data['y'] = [1 - value, parseFloat(value)];
        source.change.emit();
    '''
    return js


def slider_change(event):
    ss.exec_js(change_value(event.value))

ss.slider('Probability of Success \(p\)', 0.0, 1.0, 0.5, onchange=slider_change, triggerOnUpdate = True)
