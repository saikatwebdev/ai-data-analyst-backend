import pandas as pd


def validate_dataframe(df: pd.DataFrame)->list[str]:

    errors = []

    if df.empty:
        errors.append("Dataset is Empty")
    if len(df.columns) == 0:
        errors.append("Dataset contains no columns")
    return errors
