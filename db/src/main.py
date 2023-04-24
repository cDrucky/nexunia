from flask import Flask, request
from dash import Dash, page_container
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from viz import get_elements, full_params_query, get_single_element
from dash.dependencies import Input, Output
from views import my_blueprint
from layouts import update_layout
from components import (
    social_footer,
    make_lifecycle,
    header,
    services,
    notes,
    lifecycle_label,
)
from objects import UrlParams

cyto.load_extra_layouts()


info = "static/info.svg"

_url_params = UrlParams()

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
]


app = Flask(__name__)
app.register_blueprint(my_blueprint)

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


@app.route("/update")
def update_elements():
    location = request.args.getlist("location")
    lifecycle = request.args.getlist("lifecycle")
    services = request.args.getlist("services")

    _url_params.location = location
    _url_params.lifecycle = lifecycle
    _url_params.services = services

    updated_query = full_params_query(
        location=location, lifecycle=lifecycle, services=services
    )
    updated_elements = get_elements(updated_query)
    update_layout(dash_app, updated_elements)
    return dash_app.index()


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

