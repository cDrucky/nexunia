from py2neo import Relationship, Node
from .business_lifecycles import BusinessLifecycles
from .locations import Locations
from utils import graph as _graph
from .services import Services


def create_org_nodes(orgs):
    for org in orgs:
        node = Node("Organization", name=org.name, address=org.address, notes=org.notes,
                    website=org.website, parent_organization_1=org.parent_organization_1,
                    parent_organization_2=org.parent_organization_2, parent_organization_3=org.parent_organization_3,
                    linkedin=org.linkedin, twitter=org.twitter, instagram=org.instagram, facebook=org.facebook,
                    tiktok=org.tiktok)
        yield node


def add_organization(org_node, graph=_graph):
    graph.merge(org_node, "Organization", "name")
    print("Added: ", org_node["name"])


def get_location_node(graph, location_name):
    return graph.nodes.match("Location", name=location_name).first()


def get_lifecycle_node(graph, lifecycle_name):
    return graph.nodes.match("Lifecycle", name=lifecycle_name).first()


def create_org_location_connection(org, graph=_graph):
    org_node = graph.nodes.match("Organization", name=org.name).first()
    for location in Locations:
        if location.value in org.serviced_locations:
            location_node = get_location_node(graph, location.value)
            relationship = Relationship(org_node, "SERVICES", location_node)
            graph.merge(relationship, "SERVICES", "name")


def create_org_lifecycle_connection(org, graph=_graph):
    org_node = graph.nodes.match("Organization", name=org.name).first()

    for stages in BusinessLifecycles:
        if stages.value in org.lifecycle_stage:
            stage_node = get_lifecycle_node(graph, stages.value)
            relationship = Relationship(org_node, "PROVIDES", stage_node)
            graph.merge(relationship, "PROVIDES", "name")


def create_org_service_connection(org, graph=_graph):
    org_node = graph.nodes.match("Organization", name=org.name).first()

    for service in Services:
        if service.value in org.services:
            service_node = get_lifecycle_node(graph, service.value)
            relationship = Relationship(org_node, "HANDLES", service_node)
            graph.merge(relationship, "HANDLES", "name")


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


def create_service_node(graph=_graph):
    services = [serv.value for serv in list(Services)]
    nodes = [Node("Service", name=s) for s in services]
    for node in nodes:
        graph.merge(node, "Service", "name")



