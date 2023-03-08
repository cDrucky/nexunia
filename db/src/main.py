from flask import Flask, jsonify
from dash import Dash
import dash_cytoscape as cyto
from viz import elements
from initializer import initialize_app
from viz.stylesheets import default_stylesheet
from dash.dependencies import Input, Output
from views import my_blueprint


app = Flask(__name__)
app.register_blueprint(my_blueprint)

dash_app = Dash(__name__, server=app)

# Define the layout of the Dash app
dash_app.layout = cyto.Cytoscape(
    id='cytoscape-graph',
    style={'width': '100%', 'height': '100vh'},
    elements=elements,
    stylesheet=default_stylesheet,
)


@dash_app.callback(
    Output('cytoscape-graph', 'stylesheet'),
    Input('cytoscape-graph', 'tapNodeData')
)
def update_stylesheet(node_data):
    print(node_data)
    if node_data is None:
        # No node is selected
        return default_stylesheet
    elif node_data['node_type'] == "Organization":
        # A node is selected
        node_color = node_data['node_color']
        return [
            {
                'selector': f'node[id="{node_data["id"]}"]',
                'style': {
                    "label": "data(label)",
                    'width': '60px',
                    'height': '60px',
                    'border-width': '2px',
                    'background-color': node_color
                }
            },
            {
                "selector": "node[node_color]",
                "style": {
                    "label": "data(label)",
                    "color": "black",
                    "text-valign": "center",
                    "text-halign": "center",
                    "background-color": "data(node_color)",
                    "opacity": 0.65,
                    "z-index": 9999,
                },
            },
            {
                "selector": "node[!node_color]",
                "style": {
                    "label": "data(label)",
                    "color": "black",
                    "text-valign": "center",
                    "text-halign": "center",
                    "background-color": "grey",
                    "opacity": 0.65,
                    "z-index": 9999,
                },
            },
            {
                'selector': f'node[id="{node_data["id"]}"]:selected',
                'style': {
                    "label": f'{node_data["label"]}\nWebsite: {node_data["website"]}\nAddress: {node_data["address"]}\nNotes: {node_data["notes"]}',
                    'width': '100px',
                    'height': '100px',
                    'border-width': '5px',
                    'border-color': 'black',
                    'background-color': node_color
                }
            },

            {
                'selector': f'node[id="{node_data["id"]}"]:selected > label',
                'style': {
                    'label': 'data(label)',
                    'font-size': '20px',
                    'text-wrap': 'wrap',
                    'text-max-width': '180px',
                    'text-valign': 'top',
                    'background-color': node_color
        }
            },
            {
                'selector': f'node[id="{node_data["id"]}"]:selected > label+data(website)',
                'style': {
                    'content': f"{node_data['website']}",
                    'text-wrap': 'wrap',
                    'text-max-width': '180px',
                    'text-valign': 'top',
                    'background-color': node_color
        }
            },
            {
                'selector': f'node[id="{node_data["id"]}"]:selected > label+data(address)',
                'style': {
                    'content': f"{node_data['address']}",
                    'text-wrap': 'wrap',
                    'text-max-width': '180px',
                    'text-valign': 'bottom',
                    'background-color': node_color
                }
            },
            {
                'selector': f'node[id="{node_data["id"]}"]:selected > label+data(notes)',
                'style': {
                    'content': f"{node_data['notes']}",
                    'text-wrap': 'wrap',
                    'text-max-width': '180px',
                    'text-valign': 'top',
                    'label': 'data(notes)',
                    'background-color': node_color
                }
            },

            {
                'selector': 'node.selected',
                'style': {
                    'border-color': 'black',
                    'border-width': '2px'
                }
            }
        ]


if __name__ == '__main__':
    app.run(debug=True)




