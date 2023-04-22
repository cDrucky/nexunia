from flask import Flask, request
from dash import Dash, html
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from viz import get_elements, full_params_query, default_query, get_single_element
from viz.stylesheets import default_stylesheet
from dash.dependencies import Input, Output, State
from views import my_blueprint
from layouts.layout_manager import update_layout
from components import social_footer, make_lifecycle, header, services, notes, lifecycle_label
from objects import UrlParams

cyto.load_extra_layouts()


info = 'static/info.svg'

_url_params = UrlParams()

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
    'https://use.fontawesome.com/releases/v5.15.3/css/all.css',  # Font Awesome stylesheet
    "fontawesome_free/js/all.min.js"
]


app = Flask(__name__)
app.register_blueprint(my_blueprint)

dash_app = Dash(__name__, server=app, external_stylesheets=external_stylesheets)

# Define the layout of the Dash app
dash_app.layout = dbc.Container([cyto.Cytoscape(
    id='cytoscape-graph',
    style={'width': '100vw', 'height': '100vh'},
    elements=get_elements(default_query),
    layout={
        'name': 'cose-bilkent',
        'minNodeSpacing': 1200,
        'spacingFactor': 1.5,
        'boundingBox': {'x1': -500, 'y1': -500, 'x2': 1500, 'y2': 1500},
        'nodeOverlap': -10,
        'nodeRepulsion': 1000000,
    },

    stylesheet=default_stylesheet,
),
    html.Div(
        id='node-info',
        style={
            'position': 'absolute',
            'top': '0px',
            'right': '0px',
            'width': '20rem',
        }
    )]
)


def parse_elements(data):
    organization = {}
    locations = set()
    services = set()
    lifecycles = set()

    for item in data:
        n = item['data']
        if 'node_type' in n:
            if n['node_type'] == 'Organization':
                organization = n
            elif n['node_type'] == 'Location':
                locations.add(n['label'])
            elif n['node_type'] == 'Lifecycle':
                lifecycles.add(n['label'])
            elif n['node_type'] == 'Service':
                services.add(n['label'])

    return organization, locations, services, lifecycles


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
    Output('node-info', 'children'),
    Input('cytoscape-graph', 'tapNodeData'),
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
            ], id="node-info",
            style={'border': '1px solid #ddd'})
        return node_info_contents


if __name__ == '__main__':
    app.run(debug=True)
