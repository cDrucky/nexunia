query = """
MATCH (o:Organization)
WHERE o.location = 'York'
MATCH (o)-[:SERVICES]->(l:Location)
MATCH (o)-[:PROVIDES]->(lc:Lifecycle)
RETURN o, l, lc
"""


def query_builder(location, lifecycle):
    _query = "MATCH (o:Organization) "
    _query += "MATCH (o)-[:SERVICES]->(l:Location) "
    _query += f"WHERE l.name = '{location}' "
    _query += "MATCH (o)-[:PROVIDES]->(lc:Lifecycle) "
    _query += f"WHERE lc.name = '{lifecycle}' "
    _query += "RETURN o, l, lc"

    return _query
