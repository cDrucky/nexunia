from flask import Flask, request
from dash import Dash, html
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from viz import get_elements, full_params_query, default_query, get_single_element
from viz.stylesheets import default_stylesheet
from dash.dependencies import Input, Output
from views import my_blueprint
from layouts.layout_manager import update_layout

twitter = 'static/twitter.svg'
linkedin = 'static/linkedin.svg'
facebook = 'static/facebook.svg'
instagram = 'static/instagram.svg'
tiktok = 'static/tiktok.svg'



class _URL_PARAMS:
    def __init__(self):
        self.location = ""
        self.lifecycle = ""
        self.services = ""

    def __str__(self):
        return f"Location {self.location}, Lifecycle: {self.lifecycle}, Services: {self.services}"


_url_params = _URL_PARAMS()

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


def build_service_pills(items):

    return html.Span([dbc.Badge(str(service), pill=True, color="warning", className="m-2") for service in items])



import dash_bootstrap_components as dbc


def make_collapse_from_set(lifecycles):
    # Define a list of all possible lifecycles
    all_lifecycles = ["Idea", "Seed", "Startup", "Growth", "Mature", "Exit"]
    # Create an empty list to store the Collapse components
    collapses = []
    # Iterate over all lifecycles and create a Collapse component for each
    for lifecycle in all_lifecycles:
        # Determine whether the Collapse should be initially open and/or disabled
        if lifecycle in lifecycles:
            style = {}
        else:
            style = {"color": "lightgrey"}
        # Create the Collapse component
        collapse = dbc.Collapse(
            [
                dbc.CardBody(lifecycle)
            ],
            id=f"collapse-{lifecycle}",
            is_open=True,
            style=style,
        )
        collapses.append(collapse)
    return dbc.CardBody(collapses, style={"border": "none"})


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
def display_node_info(node_data,):
    if node_data is None:
        return None
    else:
        elements = get_elements(get_single_element(node_data["label"]))
        o, l, s, lc = parse_elements(elements)

        node_info_contents = dbc.Card(
            [
                dbc.CardHeader([html.H3(html.A(o['label'], href=o["website"]))]),
                dbc.CardBody(o["notes"]),
                build_service_pills(s),
                make_collapse_from_set(lc),
                dbc.CardFooter([
                    html.Img(src=twitter, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                    html.Img(src=instagram, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                    html.Img(src=facebook, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                    html.Img(src=linkedin, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                    html.Img(src=tiktok, style={'width': '16px', 'height': '16px', }, className="mx-2"),
                ]
                ),
            ], style={'border': '1px solid #ddd'})
        return node_info_contents


if __name__ == '__main__':
    app.run(debug=True)
