from utils import graph

def map_node_type_to_color(node_type):
    type_to_color = {
        'Organization': 'red',
        'Location': 'blue',
        'Lifecycle': 'green',
        'Service': 'yellow'
    }
    return type_to_color.get(node_type, 'gray')


def map_node_type_to_radius(node_type):
    type_to_concentricity = {
        'Organization': 1,
        'Location': 2,
        'Lifecycle': 2,
        'Service': 2
    }
    return type_to_concentricity.get(node_type, 1)



def get_nodes(record, nodes):
    node_types = {
        'o': 'Organization',
        'l': 'Location',
        'lc': 'Lifecycle',
        's': 'Service'
    }
    print("Record:", record)
    for node_type, label_attr in node_types.items():
        if record[node_type] is not None:
            if record[node_type].identity not in [node['data']['id'] for node in nodes]:
                nodes.append({
                    'data': {
                        'id': str(record[node_type].identity),
                        'label': record[node_type]['name'],
                        'website': record[node_type]['website'] if node_type == 'o' else None,
                        'notes': record[node_type]['notes'] if node_type == 'o' else None,
                        'address': record[node_type]['address'] if node_type == 'l' else None,
                        'node_type': label_attr,
                        'node_color': map_node_type_to_color(label_attr),
                        'concentricity': map_node_type_to_radius(label_attr)
                    }
                })


def get_edges(record, edges):
    if record['s'] is not None:
        edge_data = {
            f"{record['o'].identity}-SERVICES->{record['l'].identity}": {
                'source': str(record['o'].identity),
                'target': str(record['l'].identity)
            },
            f"{record['o'].identity}-PROVIDES->{record['lc'].identity}": {
                'source': str(record['o'].identity),
                'target': str(record['lc'].identity)
            },
            f"{record['o'].identity}-HANDLES->{record['s'].identity}": {
                'source': str(record['o'].identity),
                'target': str(record['s'].identity)
            }
        }
    else:
        edge_data = {
            f"{record['o'].identity}-SERVICES->{record['l'].identity}": {
                'source': str(record['o'].identity),
                'target': str(record['l'].identity)
            },
            f"{record['o'].identity}-PROVIDES->{record['lc'].identity}": {
                'source': str(record['o'].identity),
                'target': str(record['lc'].identity)
            }
        }

    for edge_id, edge in edge_data.items():
        if edge_id not in [edge['data']['id'] for edge in edges]:
            edges.append({
                'data': {
                    'id': edge_id,
                    **edge
                }
            })


def get_elements(query):
    results = graph.run(query)

    nodes = []
    edges = []

    for record in results:
        get_nodes(record, nodes)
        get_edges(record, edges)

    elements = nodes + edges
    return elements
