import pandas as pd


def detect_outliers(df: pd.DataFrame)->dict:

    numerical_df = df.select_dtypes(
        include="number"
    )


    results = {}



    for column in numerical_df.columns:
        series = numerical_df[column].dropna()

        if series.empty:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr


        outliers = series[
            (series < lower_bound) |
            (series > upper_bound)
        ]
        results[column] = {
            "q1": float(q1),
            "q3": float(q3),
            "iqr": float(iqr),
            "lower_bound": float(lower_bound),
            "upper_bound": float(upper_bound),
            "outlier_count": float(len(outliers))
        }

    return results
