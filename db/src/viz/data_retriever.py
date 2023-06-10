from utils import make_graph
import smtplib
from email.message import EmailMessage
import py2neo



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

    graph = make_graph()
    try:
        results = graph.run(query)
    except py2neo.errors.ServiceUnavailable as e:
        # Send email alert
        msg = EmailMessage()
        msg.set_content("Neo4j database is unavailable." + query)
        msg['Subject'] = "BOUNCE APP"
        msg['From'] = "wrv.brc.marketing@gmail.com"
        msg['To'] = "cldruckemiller@gmail.com"

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "wrv.brc.marketing@gmail.com"
        smtp_password = "kybrlwdywbixltth"
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.send_message(msg)
        # Raise exception again to handle it in the calling function
        raise e

    nodes = []
    edges = []

    for record in results:
        get_nodes(record, nodes)
        get_edges(record, edges)

    elements = nodes + edges
    return elements


