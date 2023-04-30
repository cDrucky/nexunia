from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from viz import get_elements, full_params_query
from viz.stylesheets import default_stylesheet


def title():
    return "Graph Page"


def description():
    return "Ecosystem Map in CytoScape"


register_page(
    __name__,
    title=title,
    description=description,
    path="/update",
)


def layout(location=None, lifecycle=None, services=None, **other_unknown_query_strings):
    if location and lifecycle and services:
        location = location.split(",")
        services = services.split(",")
        query = full_params_query(location,[lifecycle], services)
        elements = get_elements(query)
        return html.Div([
            cyto.Cytoscape(
                id="cytoscape-graph",
                style={"width": "100vw", "height": "100vh"},
                elements=elements,
                layout={
                    'name': 'circle',
                    'minNodeSpacing': 200,
                    'spacingFactor': 2,
                    'animate': True,
                    'animationDuration': 500,
                    'animationEasing': 'ease-in-out',
                    'boundingBox': {'x1': -500, 'y1': -500, 'x2': 500, 'y2': 500}
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
                            href=f"/print?location={location}&lifecycle={lifecycle}&services={services}",
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
