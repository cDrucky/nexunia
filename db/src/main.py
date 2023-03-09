from flask import Flask
from dash import Dash
import dash_cytoscape as cyto
from viz import elements
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
    elements=elements,
    stylesheet=default_stylesheet,
)


@dash_app.callback(
    Output('cytoscape-graph', 'stylesheet'),
    Input('cytoscape-graph', 'tapNodeData')
)
def update_stylesheet(node_data):
    return update_stylesheet_callback(node_data)


if __name__ == '__main__':
    app.run(debug=True)




