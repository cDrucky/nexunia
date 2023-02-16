from .sheet_reader import get_df, get_file, build_organization


sheet = get_file()
df = get_df(sheet, 6)

orgs = df.apply(build_organization, axis=1)



