import pandas as pd
# the main challange: we can't assume this category columns as same as what I added like revenue category. It might not present in the other csv/xlsx file. We need one AI layer to detect the preferred categroy columns

def revenue_by_category(
        df:pd.DataFrame,
        category_column: str,
        revenue_column:str,
)->dict:
    result= (
        df.groupby(category_column)[revenue_column]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        "labels": result.index.astype(str).tolist(),
        "values": result.astype(float).tolist(),
    }