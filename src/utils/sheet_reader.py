import pandas as pd
import os
from objects import Organization
from .locations import Locations
from .business_lifecycles import BusinessLifecycles


def get_file(filename="Organizations for Ecosystem Analysis.xlsx"):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    organization_xl_path = os.path.join(current_dir, '..', '..', 'data', filename)

    return organization_xl_path


def get_df(file, header):
    df = pd.read_excel(file, header=header)
    df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
    return df


def build_organization(df_row):
    services = [df_row["Service 1"], df_row["Service 2"], df_row["Service 3"],
                df_row["Service 4"], df_row["Service 5"]]
    business_lifecycle = [df_row["Idea"], df_row["Seed"], df_row["Startup"],
                          df_row["Growth"], df_row["Mature"], df_row["Exit"]]
    serviced_locations = [
        Locations.HARRISBURG.value if df_row["Harrisburg"] == 1 else "",
        Locations.YORK.value if df_row["Harrisburg"] == 1 else "",
        Locations.LANCASTER.value if df_row["Harrisburg"] == 1 else ""
    ]
    services_rendered = [
        BusinessLifecycles.IDEA.value if df_row["Idea"] == 1 else "",
        BusinessLifecycles.SEED.value if df_row["Seed"] == 1 else "",
        BusinessLifecycles.STARTUP.value if df_row["Startup"] == 1 else "",
        BusinessLifecycles.GROWTH.value if df_row["Growth"] == 1 else "",
        BusinessLifecycles.MATURE.value if df_row["Mature"] == 1 else "",
        BusinessLifecycles.EXIT.value if df_row["Exit"] == 1 else "",
    ]
    return Organization(df_row['ID'], df_row['Organization'], df_row['Address'],
                        df_row['Location'], df_row['Notes'], df_row['Website'], df_row['Parent Organization'],
                        ["Industry"], services, business_lifecycle, serviced_locations, services_rendered)


