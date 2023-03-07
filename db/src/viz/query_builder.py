query = """
MATCH (o:Organization)
WHERE o.location = 'York'
MATCH (o)-[:SERVICES]->(l:Location)
MATCH (o)-[:PROVIDES]->(lc:Lifecycle)
RETURN o, l, lc
"""