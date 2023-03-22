from flask import Flask, request, redirect, url_for
from dash import Dash
import dash_cytoscape as cyto
from viz import get_elements, query_builder, default_query
from viz.callbacks import update_stylesheet_callback
from viz.stylesheets import default_stylesheet
from dash.dependencies import Input, Output
from views import my_blueprint

app = Flask(__name__)
app.register_blueprint(my_blueprint)

dash_app = Dash(__name__, server=app)

# Define the layout of the Dash app
dash_app.layout = cyto.Cytoscape(
    id='cytoscape-graph',
    style={'width': '100%', 'height': '100vh'},
    elements=get_elements(default_query),
    layout={
        'name': 'concentric',
        'minNodeSpacing': 80,
        'spacingFactor': 1.5,
        'animate': False,
        'animationDuration': 500,
        'animationEasing': 'ease-in-out',
        'boundingBox': {'x1': -500, 'y1': -500, 'x2': 500, 'y2': 500},
    },

    stylesheet=default_stylesheet,
)


def get_concentricity(ele):
    return ele.get('data').get('concentricity', 1)

@app.route('/update')
def update_elements():
    location = request.args.getlist('location')
    lifecycle = request.args.getlist('lifecycle')
    services = request.args.getlist('services')

    updated_query = query_builder(location=location, lifecycle=lifecycle, services=services)
    updated_elements = get_elements(updated_query)
    dash_app.layout = cyto.Cytoscape(
        id='cytoscape-graph',
        style={'width': '100%', 'height': '100vh'},
        elements=updated_elements,
        layout={
                    'name': 'concentric',
                    'minNodeSpacing': 80,
                    'spacingFactor': 1.5,
                    'animate': False,
                    'animationDuration': 500,
                    'animationEasing': 'ease-in-out',
                    'boundingBox': {'x1': -500, 'y1': -500, 'x2': 500, 'y2': 500}
                },
        stylesheet=default_stylesheet,
    )
    return dash_app.index()

@dash_app.callback(
    Output('cytoscape-graph', 'stylesheet'),
    Input('cytoscape-graph', 'tapNodeData')
)
def update_stylesheet(node_data):
    return update_stylesheet_callback(node_data)


if __name__ == '__main__':
    app.run(debug=True)
