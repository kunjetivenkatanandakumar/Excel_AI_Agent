import pandas as pd

def clean_dataframe(df):

    df = df.drop_duplicates()

    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
            )

        if pd.api.types.is_numeric_dtype(
            df[col]
        ):

            df[col] = df[col].fillna(
                df[col].median()
            )

    return df