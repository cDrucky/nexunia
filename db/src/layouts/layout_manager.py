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
            style={
                'position': 'absolute',
                'top': '0px',
                'right': '0px',
                'width': '20rem',
                'height': '100%'
            }
        )],
        # Use media queries to adjust the positioning of the 'node-info' Div
        style={
            '@media (max-width: 767px)': {
                '#node-info': {
                    'position': 'fixed',
                    'width': '100%',
                    'height': '20rem',
                    'bottom': '0px',
                    'right': 'auto',
                    'left': '0px',
                    'background-color': 'white'
                }
            }
        }

    )
