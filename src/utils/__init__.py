from sheet_reader import get_df, get_file, build_organization
from db_connector import add_organization, connect_org_location, connect_org_service

sheet = get_file()
df = get_df(sheet, 6)

orgs = df.apply(build_organization, axis=1)
