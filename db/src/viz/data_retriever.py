from utils import graph
from .query_builder import query

results = graph.run(query)

# Define a dictionary to map node_type to color
type_to_color = {
    'Organization': 'red',
    'Location': 'blue',
    'Lifecycle': 'green'
}

# Convert the results into a format that Dash Cytoscape can understand
nodes = []
edges = []

for record in results:
    # Add nodes to the list
    if record['o'].identity not in [node['data']['id'] for node in nodes]:
        node_type = 'Organization'
        nodes.append({
            'data': {
                'id': str(record['o'].identity),
                'label': record['o']['name'],
                'website': record['o']['website'],
                'notes': record['o']['notes'],
                'address': record['o']['address'],
                'node_type': node_type,
                'node_color': type_to_color.get(node_type, 'gray')
            }
        })
    if record['l'].identity not in [node['data']['id'] for node in nodes]:
        node_type = 'Location'
        nodes.append({
            'data': {
                'id': str(record['l'].identity),
                'label': record['l']['name'],
                'node_type': node_type,
                'node_color': type_to_color.get(node_type, 'gray')
            }
        })
    if record['lc'].identity not in [node['data']['id'] for node in nodes]:
        node_type = 'Lifecycle'
        nodes.append({
            'data': {
                'id': str(record['lc'].identity),
                'label': record['lc']['name'],
                'node_type': node_type,
                'node_color': type_to_color.get(node_type, 'gray')
            }
        })

    # Add edges to the list

    edges.append({
        'data': {
            'id': f"{record['o'].identity}-SERVICES->{record['l'].identity}",
            'source': str(record['o'].identity),
            'target': str(record['l'].identity)
        }
    })

    edges.append({
        'data': {
            'id': f"{record['o'].identity}-PROVIDES->{record['lc'].identity}",
            'source': str(record['o'].identity),
            'target': str(record['lc'].identity)
        }
    })

# Combine the nodes and edges into a single list
elements = nodes + edges
