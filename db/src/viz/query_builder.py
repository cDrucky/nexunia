default_query = """
MATCH (o:Organization)
MATCH (o)-[:SERVICES]->(l:Location)
MATCH (o)-[:PROVIDES]->(lc:Lifecycle)
MATCH (o)-[:HANDLES]->(s:Service)
RETURN o, l, lc, s
"""


def full_params_query(location="Harrisburg", lifecycle="Growth", services="Funding", **kwargs):
    _query = "MATCH (o:Organization) "
    _query += "MATCH (o)-[:SERVICES]->(l:Location) "
    _query += f"WHERE l.name in {location} "
    _query += "MATCH (o)-[:PROVIDES]->(lc:Lifecycle) "
    _query += f"WHERE lc.name in {lifecycle} "
    _query += "MATCH (o)-[:HANDLES]->(s:Service) "
    _query += f"WHERE s.name IN {services} "
    _query += "RETURN o, l, lc, s"
    return _query

# def service_expansion_query(organization_name, location, lifecycle):
#     query = (
#         f"MATCH (o:Organization)-[:SERVICES]->(l:Location) WHERE l.name = '{location}' "
#         f"MATCH (o)-[:PROVIDES]->(lc:Lifecycle) WHERE lc.name = '{lifecycle}' "
#         f"MATCH (o)-[:HANDLES]->(s:Service) WHERE o.name = '{organization_name}' "
#         "RETURN o, l, lc, s"
#     )
#     print(query)
#     return query


def service_expansion_query(organization_name, location, lifecycle):
    query = (
        f"MATCH (l:Location {{name: '{location}'}})<-[:SERVICES]-(o:Organization)-[:PROVIDES]->(lc:Lifecycle {{name: '{lifecycle}'}})\n"
        f"OPTIONAL MATCH (o)-[:HANDLES]->(s:Service)\n"
        f"WHERE o.name = '{organization_name}'\n"
        "RETURN o, l, lc, s"
    )
    # print(query)
    return query



