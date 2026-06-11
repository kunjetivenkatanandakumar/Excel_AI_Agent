def profile_dataframe(df):

    profile = {}

    profile["rows"] = len(df)

    profile["columns"] = len(df.columns)

    profile["missing"] = (
        df.isnull().sum().sum()
    )

    profile["duplicates"] = (
        df.duplicated().sum()
    )

    return profile