from dash import html, register_page, dcc
import dash_cytoscape as cyto
from viz import get_elements, default_query
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
    ])
