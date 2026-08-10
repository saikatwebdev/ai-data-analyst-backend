import numpy as np
import pandas as pd



def numerical_summary(df:pd.DataFrame)->dict:


    numerical_df = df.select_dtypes(
        include="number"
    )

    results = {}

    for column in numerical_df.columns:


        values = numerical_df[column].dropna().to_numpy()

        if len(values) == 0:
            continue

        results[column] = {
            "mean": float(np.mean(values)),
            "median": float(np.median(values)),
            "std": float(np.std(values)),
            "min": float(np.min(values)),
            "max": float(np.max(values)),
            "q25": float(np.quantile(values,.25)),
            "q75":float(np.quantile(values,.75)),
        }

    return results