#Import Cyto and Dash
import json

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import dash_cytoscape as cyto

def load_json(st):
    if 'http' in st:
        return requests.get(st).json()
    else:
        with open(st, 'rb') as f:
            x = json.load(f)
        return x

app = dash.Dash(__name__)
server = app.server

#import elements list
with open("vamp2_500_connections.txt", "r") as el:
    my_elements = json.load(el)

#import stylesheet document
with open("my_stylesheet.txt", "r") as st:
    my_stylesheet = json.load(st)

stylesheet = my_stylesheet
elements = my_elements

styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': '100%',
        'width': '100%'
    },
    'cy-container': {
        'flex': '1',
        'position': 'relative'
    },
    'cytoscape': {
        'position': 'absolute',
        'width': '100%',
        'height': '100%',
        'z-index': 999
    }
}

# App
app.layout = html.Div(style=styles['container'], children=[
    html.Div([
        html.Button("Responsive Toggle", id='toggle-button'),
        html.Div(id='toggle-text')
    ]),
    html.Div(className='cy-container', style=styles['cy-container'], children=[
        cyto.Cytoscape(
            id='cytoscape-responsive-layout',
            elements=elements,
            stylesheet=stylesheet,
            style=styles['cytoscape'],
            layout={
                'name': 'cose',
                'idealEdgeLength': 100,
                'nodeOverlap': 20,
                'refresh': 20,
                'fit': True,
                'padding': 30,
                'randomize': False,
                'componentSpacing': 100,
                'nodeRepulsion': 400000,
                'edgeElasticity': 100,
                'nestingFactor': 5,
                'gravity': 80,
                'numIter': 1000,
                'initialTemp': 200,
                'coolingFactor': 0.95,
                'minTemp': 1.0
            },
            responsive=True
        )
    ])
])


@app.callback(Output('cytoscape', 'responsive'), Input('toggle-button', 'n_clicks'))
def toggle_responsive(n_clicks):
    n_clicks = 2 if n_clicks is None else n_clicks
    toggle_on = n_clicks % 2 == 0
    return toggle_on


@app.callback(Output('toggle-text', 'children'), Input('cytoscape', 'responsive'))
def update_toggle_text(responsive):
    return '\t' + 'Responsive ' + ('On' if responsive else 'Off')


if __name__ == '__main__':
    app.run_server(debug=True)