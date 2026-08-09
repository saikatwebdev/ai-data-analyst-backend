import pandas as pd


def numerical_statistics(df: pd.DataFrame)-> dict:

    numerical_df = df.select_dtypes(
        include="number"
    )


    statistics = {}

    for column in numerical_df.columns:


        series = numerical_df[column]

        statistics[column] = {
            "count": int(series.count()),
            "mean": float(series.mean()),
            "median": float(series.median()),
            "std": float(series.std()),
            "min": float(series.min()),
            "max": float(series.max()),
        }

    return statistics