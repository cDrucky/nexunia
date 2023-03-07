from flask import Flask, jsonify
from dash import Dash
import dash_cytoscape as cyto
from viz import elements
from initializer import initialize_app
from viz import stylesheet


app = Flask(__name__)
dash_app = Dash(__name__, server=app)


# Define the layout of the Dash app
dash_app.layout = cyto.Cytoscape(
    id='cytoscape-graph',
    style={'width': '100%', 'height': '500px'},
    elements=elements,
    stylesheet=stylesheet,
)


@app.route('/initialize')
def initialize():
    initialize_app()
    return jsonify({'message': 'App initialized successfully'})


if __name__ == '__main__':
    app.run(debug=True)




