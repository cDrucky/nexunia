import dash_cytoscape as cyto
from viz.stylesheets import default_stylesheet
from dash import html


def update_layout(dash_app, elements):
    dash_app.layout = html.Div([cyto.Cytoscape(
        id='cytoscape-graph',
        style={'width': '100%', 'height': '100vh'},
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
        stylesheet=default_stylesheet, ),

        html.Div(
            id='node-info',
            style={'position': 'absolute', 'top': '0px', 'right': '0px', 'width': '400px', 'height': '100%'}
        )]
    )
