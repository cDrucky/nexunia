from flask import Flask
from dash import Dash, page_container
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from callbacks import display_node_info

cyto.load_extra_layouts()

info = "static/info.svg"

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
    "static/custom.css"
]

app = Flask(__name__)

dash_app = Dash(__name__, server=app, external_stylesheets=external_stylesheets, use_pages=True)

dash_app.layout = dbc.Container(
    [
        page_container
    ]
)

dash_app.callback(
    Output("node-info", "children"),
    Input("cytoscape-graph", "tapNodeData"),
)(display_node_info)

if __name__ == "__main__":
    app.run(debug=True)
