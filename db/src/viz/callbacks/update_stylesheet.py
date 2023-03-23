from viz.stylesheets import default_stylesheet
from viz import get_elements, service_expansion_query
from layouts.layout_manager import update_layout


def focus_node_callback(node_data, location, lifecycle, dash_app):
    if node_data is None:
        # No node is selected
        return default_stylesheet
    elif node_data['node_type'] == "Organization":
        # A node is selected
        node_color = node_data['node_color']
        print(location, lifecycle)
        query = service_expansion_query(node_data['label'], location, lifecycle)
        elements = get_elements(query)
        return elements
        '''return [
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
        ]'''