import pandas as pd
import os
from objects import Organization

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
    return Organization(df_row['ID'], df_row['Organization'], df_row['Address'],
                        df_row['Location'], df_row['Notes'], df_row['Website'], df_row['Parent Organization'],
                        ["Industry"], services, business_lifecycle)


sheet = get_file()
df = get_df(sheet, 6)

orgs = df.apply(build_organization, axis=1)
print(orgs[0])
