import pandas as pd
import os
from objects import Organization
from .locations import Locations
from .business_lifecycles import BusinessLifecycles


def get_file(filename="Organizations for Ecosystem Analysis.xlsx"):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    organization_xl_path = os.path.join(current_dir, '..', '..', '..', 'data', filename)

    return organization_xl_path


def get_df(file, header):
    df = pd.read_excel(file, header=header)
    df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
    return df


def build_organization(df_row):

    serviced_locations = []
    if df_row[Locations.HARRISBURG.value] == "1": serviced_locations.append(Locations.HARRISBURG.value)
    if df_row[Locations.YORK.value] == "1": serviced_locations.append(Locations.YORK.value)
    if df_row[Locations.LANCASTER.value] == "1": serviced_locations.append(Locations.LANCASTER.value)


    lifecycle_stages = []
    if df_row["Idea"] == 1: lifecycle_stages.append(BusinessLifecycles.IDEA.value)
    if df_row["Seed"] == 1: lifecycle_stages.append(BusinessLifecycles.SEED.value)
    if df_row["Startup"] == 1: lifecycle_stages.append(BusinessLifecycles.STARTUP.value)
    if df_row["Growth"] == 1: lifecycle_stages.append(BusinessLifecycles.GROWTH.value)
    if df_row["Mature"] == 1: lifecycle_stages.append(BusinessLifecycles.MATURE.value)
    if df_row["Exit"] == 1: lifecycle_stages.append(BusinessLifecycles.EXIT.value)

    services = []
    for col in ["Service 1", "Service 2", "Service 3", "Service 4", "Service 5"]:
        if df_row[col] != "":
            services.append(df_row[col])

    return Organization(df_row['Organization'], serviced_locations, df_row["Parent 1"], df_row["Parent 2"],
                        df_row["Parent 3"], df_row['Address'], df_row['Website'], df_row['Notes'], lifecycle_stages,
                        services, df_row['LinkedIn'], df_row['Twitter'], df_row['Instagram'], df_row['Facebook'],
                        df_row['TikTok'])

