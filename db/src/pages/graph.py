from dash import html, register_page, dcc
import dash_cytoscape as cyto
from viz import get_elements, default_query
from viz.stylesheets import default_stylesheet
import random


def repulsion():
    return random.randint(999000, 10001000)


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
            style={"width": "100%", "height": "100vh"},
            elements=get_elements(default_query),
            layout={
                "name": "cose-bilkent",
                "minNodeSpacing": 1200,
                "spacingFactor": 1.5,
                "boundingBox": {"x1": -500, "y1": -500, "x2": 1500, "y2": 1500},
                "nodeOverlap": -10,
                "nodeRepulsion": 1000000,
            },
            minZoom=0.3,
            maxZoom=1.5,
            zoom=1.3,
            stylesheet=default_stylesheet,
            responsive=True,
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
    ])
