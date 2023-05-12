from utils import graph


def map_node_type_to_color(node_type):
    type_to_color = {
        'Location': '#E9675B',
        'Organization': '#5BBBCF',
        'Lifecycle': '#ED894A',
        'Service': '#F7D162'
    }
    return type_to_color.get(node_type, 'gray')


def get_nodes(record, nodes):
    node_types = {
        'o': 'Organization',
        'l': 'Location',
        'lc': 'Lifecycle',
        's': 'Service'
    }
    for node_type, label_attr in node_types.items():
        if record.get(node_type):
            if record[node_type].identity not in [node.get('data', {}).get('id') for node in nodes]:
                nodes.append({
                    'data': {
                        'id': str(record[node_type].identity),
                        'label': record[node_type].get('name'),
                        'website': record[node_type].get('website') if node_type == 'o' else None,
                        'notes': record[node_type].get('notes') if node_type == 'o' else None,
                        'address': record[node_type].get('address') if node_type == 'o' else None,
                        'node_type': label_attr,
                        'node_color': map_node_type_to_color(label_attr),
                        'linkedin': record[node_type].get('linkedin') if node_type == 'o' else None,
                        'twitter': record[node_type].get('twitter') if node_type == 'o' else None,
                        'facebook': record[node_type].get('facebook') if node_type == 'o' else None,
                        'instagram': record[node_type].get('instagram') if node_type == 'o' else None,
                        'tiktok': record[node_type].get('tiktok') if node_type == 'o' else None,
                    }
                })


def get_edges(record, edges):
    edge_data = {}
    if record['o'] is not None and record['l'] is not None:
        edge_data[f"{record['o'].identity}-SERVICES->{record['l'].identity}"] = {
            'source': str(record['o'].identity),
            'target': str(record['l'].identity)
        }
    if record['o'] is not None and record['lc'] is not None:
        edge_data[f"{record['o'].identity}-PROVIDES->{record['lc'].identity}"] = {
            'source': str(record['o'].identity),
            'target': str(record['lc'].identity)
        }
    if record['o'] is not None and record['s'] is not None:
        edge_data[f"{record['o'].identity}-HANDLES->{record['s'].identity}"] = {
            'source': str(record['o'].identity),
            'target': str(record['s'].identity)
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

