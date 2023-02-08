from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()
database_password = os.getenv("DATABASE_PASSWORD")

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", database_password))

def add_organization(tx, org):
    tx.run("CREATE (p:Organization {name: $org.name, address: $org.address, \
        location: $org.location, id: $org.id, notes: $org.notes, website: $org.website, \
        parent_organization: $org.parent_organization })", org=org)

def connect_org_location(tx, org, location):
    tx.run("MATCH (o:Organization), (l:Location) WHERE o.name = '$org.name' \
        AND l.name = '$location.name' CREATE (o)-[r:SERVICES]->(l)", \
        org=org, location=location)
    
def connect_org_service(tx, org, service):
    tx.run("MATCH (o:Organization), (s:Service) WHERE o.name = '$org.name' \
        AND s.name = '$service.name' CREATE (o)-[r:PROVIDES]->(s)", \
        org=org, service=service)
    
        