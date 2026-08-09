import pandas as pd

def categorical_analysis(df:pd.DataFrame)-> dict:
    categorical_df = df.select_dtypes(
        include="object"
    )
    results = {}


    for column in categorical_df.columns:

        value_counts = (
            categorical_df[column]
            .value_counts(dropna=False)
            .head(20) # will change later because it is for small scale data to avoid lots of uniqe values
        )

        results[column] = {
            str(value): int(count)
            for value, count in value_counts.items()
        }

    return results
