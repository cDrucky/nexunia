from flask import Flask
from dash import Dash, page_container
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from viz import get_elements, get_single_element
from dash.dependencies import Input, Output
from components import (
    social_footer,
    make_lifecycle,
    header,
    services,
    notes,
    lifecycle_label,
)

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


def parse_elements(data):
    organization = {}
    locations = set()
    services = set()
    lifecycles = set()

    for item in data:
        n = item["data"]
        if "node_type" in n:
            if n["node_type"] == "Organization":
                organization = n
            elif n["node_type"] == "Location":
                locations.add(n["label"])
            elif n["node_type"] == "Lifecycle":
                lifecycles.add(n["label"])
            elif n["node_type"] == "Service":
                services.add(n["label"])

    return organization, locations, services, lifecycles


@dash_app.callback(
    Output("node-info", "children"),
    Input("cytoscape-graph", "tapNodeData"),
)
def display_node_info(node_data):
    if node_data is None:
        return None
    else:

        elements = get_elements(get_single_element(node_data["label"]))
        o, l, s, lc = parse_elements(elements)

        node_info_contents = dbc.Card(
            [
                header(o),
                notes(o),
                lifecycle_label(),
                services(s),
                make_lifecycle(lc),
                social_footer(o),
            ],
            id="node-info",
            style={"border": "1px solid #ddd"},
        )
        return node_info_contents


if __name__ == "__main__":
    app.run(debug=True)

