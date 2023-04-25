default_query = """
MATCH (o:Organization)
OPTIONAL MATCH (o)-[:SERVICES]->(l:Location)
OPTIONAL MATCH (o)-[:PROVIDES]->(lc:Lifecycle)
OPTIONAL MATCH (o)-[:HANDLES]->(s:Service)
RETURN o, l, lc, s
"""


def full_params_query(location="Harrisburg", lifecycle="Growth", services="Funding", **kwargs):
    _query = "MATCH (o:Organization) "
    _query += "MATCH (o)-[:SERVICES]->(l:Location) "
    _query += f"WHERE l.name in {location} "
    _query += "MATCH (o)-[:PROVIDES]->(lc:Lifecycle) "
    _query += f"WHERE lc.name in {lifecycle} "
    _query += "MATCH (o)-[:HANDLES]->(Service) "
    _query += f"WHERE Service.name IN {services} "
    _query += "MATCH (o)-[:HANDLES]->(s:Service) "
    _query += "RETURN o, l, lc, s"
    return _query


def service_expansion_query(organization_name, location, lifecycle):
    query = (
        f"MATCH (l:Location {{name: '{location}'}})<-[:SERVICES]-(o:Organization)-[:PROVIDES]->(lc:Lifecycle {{name: '{lifecycle}'}})\n"
        f"OPTIONAL MATCH (o)-[:HANDLES]->(s:Service)\n"
        f"WHERE o.name = '{organization_name}'\n"
        "RETURN o, l, lc, s"
    )
    return query


def get_single_element(organization_name):
    query = (
        f"MATCH (o:Organization {{name: '{organization_name}'}})"
        f"OPTIONAL MATCH (o)-[:PROVIDES]->(lc:Lifecycle)\n"
        f"OPTIONAL MATCH (o)-[:HANDLES]->(s:Service)\n"
        f"OPTIONAL MATCH (o)-[:SERVICES]->(l:Location)\n"
        f"OPTIONAL MATCH (o)-[:HANDLES]->(s:Service)\n"
        "RETURN o, l, lc, s"
    )
    return query



