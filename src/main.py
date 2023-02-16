from utils import orgs
from utils.db_connector import create_org_nodes, add_organization, create_org_location_connection


def generate_org_nodes():
    org_nodes = create_org_nodes(orgs)

    for node in org_nodes:
        add_organization(node)
        
def generate_org_relationships():
    for org in orgs:
        create_org_location_connection(org)


if __name__ == '__main__':
    generate_org_nodes()
    generate_org_relationships()



