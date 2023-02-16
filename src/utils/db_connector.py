from py2neo import Graph, Relationship, Node
from dotenv import load_dotenv
from business_lifecycles import BusinessLifecycles
from locations import Locations
import os

load_dotenv()
database_password = os.getenv("DATABASE_PASSWORD")

uri = "bolt://localhost:7687"

_graph = Graph(uri, user="neo4j", password=database_password)


def create_org_nodes(orgs):
    for org in orgs:
        node = Node("Organization", name=org.name, address=org.address, location=org.location, notes=org.notes,
                    website=org.website, parent_organization=org.parent_organization)
        yield node


def add_organization(org_node, graph=_graph): graph.merge(org_node, "Organization", "name")


def create_org_location_connection(org, graph=_graph):
    pass


def create_lifecycle_node(graph=_graph):
    lifecycles = [loc.value for loc in list(BusinessLifecycles)]
    nodes = [Node("Lifecycle", name=lc) for lc in lifecycles]
    for node in nodes:
        graph.merge(node, "Lifecycle", "name")


def create_location_node(graph=_graph):
    locations = [loc.value for loc in list(Locations)]
    nodes = [Node("Location", name=loc) for loc in locations]
    for node in nodes:
        graph.merge(node, "Location", "name")


create_lifecycle_node()
create_location_node()


