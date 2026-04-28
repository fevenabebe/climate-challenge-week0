import pandas as pd
import os

countries = ["ethiopia", "sudan", "tanzania", "nigeria", "kenya"]

# get correct absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

def load_data():
    dfs = []
    for c in countries:
        file_path = os.path.join(DATA_DIR, f"{c}_clean.csv")
        df = pd.read_csv(file_path)
        df["Country"] = c.capitalize()
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)