from dotenv import load_dotenv
from py2neo import Graph
import os
from .sheet_reader import get_df, get_file, build_organization


load_dotenv()
database_password = os.getenv("DATABASE_PASSWORD")
database_user = os.getenv("DATABASE_USER")
database_uri = os.getenv("DATABASE_HOST")
graph = Graph(database_uri, user=database_user, password=database_password)
# sheet = get_file()
# df = get_df(sheet, 6)
#
# orgs = df.apply(build_organization, axis=1)
def parse_elements(data):
    organization = {}
    locations = set()
    services = set()
    lifecycles = set()

    for item in data:
        n = item["data"]
        if "node_type" in n:
            if n["node_type"] == "Organization":
                organization = n
            elif n["node_type"] == "Location":
                locations.add(n["label"])
            elif n["node_type"] == "Lifecycle":
                lifecycles.add(n["label"])
            elif n["node_type"] == "Service":
                services.add(n["label"])

    return organization, locations, services, lifecycles
