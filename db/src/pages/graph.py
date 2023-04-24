from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from viz import get_elements, full_params_query, default_query, get_single_element
from viz.stylesheets import default_stylesheet


def title():
    return "Graph Page"


def description():
    return "Ecosystem Map in CytoScape"


register_page(
    __name__,
    title=title,
    description=description,
    path="/",
)


layout = html.Div([
        cyto.Cytoscape(
            id="cytoscape-graph",
            style={"width": "100vw", "height": "100vh"},
            elements=get_elements(default_query),
            layout={
                "name": "cose-bilkent",
                "minNodeSpacing": 1200,
                "spacingFactor": 1.5,
                "boundingBox": {"x1": -500, "y1": -500, "x2": 1500, "y2": 1500},
                "nodeOverlap": -10,
                "nodeRepulsion": 1000000,
            },
            stylesheet=default_stylesheet,
        ),
        html.Div(
            id="node-info",
            style={
                "position": "absolute",
                "top": "0px",
                "right": "0px",
                "width": "20rem",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Link(
                        dbc.Button(
                            "Print",
                            id="print",
                            color="primary",
                            className="mr-1",
                        ),
                        href="/print",
                        target="_blank",
                        id="print-link",
                    ),
                ),
            ],
            style={
                "position": "absolute",
                "bottom": "20px",
                "left": "20px",
                "z-index": "1000",
            },
        ),
    ])
