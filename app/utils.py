import pandas as pd

countries = ["ethiopia", "sudan", "tanzania", "nigeria", "kenya"]

def load_data():
    dfs = []
    for c in countries:
        df = pd.read_csv(f"data/{c}_clean.csv")
        df["Country"] = c.capitalize()
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


def filter_data(df, selected_countries, year_range):
    df = df[df["Country"].isin(selected_countries)]
    df = df[(df["YEAR"] >= year_range[0]) & (df["YEAR"] <= year_range[1])]
    return df