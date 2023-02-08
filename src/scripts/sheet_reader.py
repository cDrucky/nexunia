import pandas as pd
import os



def get_file(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    organization_xl_path = os.path.join(current_dir, '..', '..', 'data', filename)
    
    return organization_xl_path



def get_df(file):
    return pd.read_excel(file)

