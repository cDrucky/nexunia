import dash
from flask import Flask, request, redirect, url_for
from dash import Dash
import dash_cytoscape as cyto
from viz import get_elements, full_params_query, default_query
from viz.callbacks import focus_node_callback
from viz.stylesheets import default_stylesheet
from dash.dependencies import Input, Output, State
from views import my_blueprint
from layouts.layout_manager import update_layout
import urllib.parse


class _URL_PARAMS:
    def __init__(self):
        self.location = ""
        self.lifecycle = ""
        self.services = ""

    def __str__(self):
        return f"Location {self.location}, Lifecycle: {self.lifecycle}, Services: {self.services}"

_url_params = _URL_PARAMS()


app = Flask(__name__)
app.register_blueprint(my_blueprint)

dash_app = Dash(__name__, server=app)

# Define the layout of the Dash app
dash_app.layout = cyto.Cytoscape(
    id='cytoscape-graph',
    style={'width': '100%', 'height': '100vh'},
    elements=get_elements(default_query),
    layout={
        'name': 'random',
        'minNodeSpacing': 80,
        'spacingFactor': 1.5,
        'animate': False,
        'animationDuration': 500,
        'animationEasing': 'ease-in-out',
        'boundingBox': {'x1': -500, 'y1': -500, 'x2': 500, 'y2': 500},
    },

    stylesheet=default_stylesheet,
)


@app.route('/update')
def update_elements():
    location = request.args.getlist('location')
    lifecycle = request.args.getlist('lifecycle')
    services = request.args.getlist('services')

    _url_params.location = location
    _url_params.lifecycle = lifecycle
    _url_params.services = services

    updated_query = full_params_query(location=location, lifecycle=lifecycle, services=services)
    updated_elements = get_elements(updated_query)
    update_layout(dash_app, updated_elements)
    return dash_app.index()

@dash_app.callback(
    Output('cytoscape-graph', 'elements'),
    Input('cytoscape-graph', 'tapNodeData'),
)
def focus_org(node_data):
    print(_url_params)
    if node_data is None:
        return dash.no_update
    else:
        elements = focus_node_callback(node_data, _url_params.location[0], _url_params.lifecycle[0], dash_app)
        update_layout(dash_app, elements)
        return elements


if __name__ == '__main__':
    app.run(debug=True)
