import pandas as pd

def profile_dataset(df: pd.DataFrame)-> dict:

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    missing_counts = df.isnull().sum()

    missing_values = {
        column: int(count)
        for column, count in df.isnull().sum().items()
        if count > 0
    }
    missing_percentage = (
        missing_counts / len(df)*100
    )

    missing_percentage = {
        column : round(float(value),2)
        for column, value in missing_percentage.items()
        if value >0
    }


    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),

        "numerical_columns": numerical_columns,
        "categorical_columns": categorical_columns,

        "data_types": {
            column: str(dtype)
            for column, dtype in df.dtypes.items()
        },

        "missing_values": missing_values,
        "missing_percentage": missing_percentage,
        "duplicate_rows": int(df.duplicated().sum()),
    }