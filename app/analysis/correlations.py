import pandas as pd

def correlation_analysis(df:pd.DataFrame)->dict:

    numerical_df = df.select_dtypes(
        include="number"
    )

    if numerical_df.shape[1]< 2:
        return {}

    correlation_matrix = numerical_df.corr()

    return {
        column:{
            other_column: round(
                float(value),
                4
            )
            for other_column, value in row.items()
        }
        for column, row in correlation_matrix.iterrows()
    }