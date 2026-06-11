import pandas as pd

def read_file(file):

    if file.name.endswith(".csv"):
        return {"Sheet1": pd.read_csv(file)}

    return pd.read_excel(
        file,
        sheet_name=None
    )