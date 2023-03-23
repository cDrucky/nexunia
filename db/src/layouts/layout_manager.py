import dash_cytoscape as cyto
from viz.stylesheets import default_stylesheet


def update_layout(dash_app, elements):
    dash_app.layout = cyto.Cytoscape(
        id='cytoscape-graph',
        style={'width': '100%', 'height': '100vh'},
        elements=elements,
        layout={
            'name': 'concentric',
            'minNodeSpacing': 80,
            'spacingFactor': 1.5,
            'animate': False,
            'animationDuration': 500,
            'animationEasing': 'ease-in-out',
            'boundingBox': {'x1': -500, 'y1': -500, 'x2': 500, 'y2': 500}
        },
        stylesheet=default_stylesheet,
    )
