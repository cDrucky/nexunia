from utils import orgs
from utils.db_connector import create_org_nodes, add_organization, create_org_location_connection, create_org_lifecycle_connection, create_lifecycle_node, create_location_node
from flask import jsonify

def generate_org_nodes():
    org_nodes = create_org_nodes(orgs)

    for node in org_nodes:
        add_organization(node)

def generate_org_relationships():
    for org in orgs:
        create_org_location_connection(org)

    for org in orgs:
        create_org_location_connection(org)
        create_org_lifecycle_connection(org)
def initialize_app():
    create_lifecycle_node()
    create_location_node()

    generate_org_nodes()
    generate_org_relationships()

