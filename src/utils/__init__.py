from .sheet_reader import get_df, get_file, build_organization
from enum import Enum

sheet = get_file()
df = get_df(sheet, 6)

orgs = df.apply(build_organization, axis=1)


class BusinessLifecycles(Enum):
    IDEA = "Idea"
    SEED = "Seed"
    STARTUP = "Startup"
    GROWTH = "Growth"
    MATURE = "Mature"
    EXIT = "Exit"

class Locations(Enum):
    HARRISBURG = "Harrisburg"
    YORK = "York"
    LANCASTER = "Lancaster"