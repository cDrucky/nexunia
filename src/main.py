from utils import orgs
from utils.db_connector import create_org_nodes, add_organization


def generate_org_nodes():
    org_nodes = create_org_nodes(orgs)

    for node in org_nodes:
        add_organization(node)


if __name__ == '__main__':
    generate_org_nodes()




