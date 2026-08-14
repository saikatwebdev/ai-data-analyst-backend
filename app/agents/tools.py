import pandas as pd

from langchain.tools import tool

from app.services.dataset_store import get_dataset
from app.analysis.outliers import detect_outliers
from app.analysis.correlations import correlation_analysis

def create_dataset_tools(dataset_id: str):

    df = get_dataset(dataset_id)

    if df is None:
        raise ValueError("Dataset not found.")

    @tool
    def get_dataset_info() -> str:
        """Return basic information about the uploaded dataset,
        including number of rows, columns, and column names."""

        return (
            f"Rows: {len(df)}\n"
            f"Columns: {len(df.columns)}\n"
            f"Column names: {', '.join(df.columns)}"
        )

    @tool
    def get_column_info()->str:
        """Return the name and data type of every column in the dataset"""

        result = []

        for column in df.columns:
            result.append(
                f"{column}: {df[column].dtype}"
            )
        return "\n".join(result)

    @tool
    def get_column_statistics(column:str)->str:

        """Return descriptive statistics for a numerical column.
        Includes count, mean, median, standard deviation, minimum,maximum, Q1 and Q3
        """

        if column not in df.columns:
            return f"Column '{column}' does not exist"

        if not pd.api.types.is_numeric_dtype(df[column]):
            return f"Column '{column}' is not numerical"

        series = df[column].dropna()

        if series.empty:
            return "Column '{column}' contain no numerical values"

        return (
            f"Column : {column}\n"
            f"Count: {series.count}\n"
            f"Mean: {series.mean():.2f}\n"
            f"Median: {series.median():.2f}\n"
            f"Standard deviation: {series.std():.2f}\n"
            f"Minimum: {series.min():.2f}\n"
            f"Maximum: {series.max():.2f}\n"
            f"Q1: {series.quantile(0.25):.2f}\n"
            f"Q3: {series.quantile(0.75):.2f}"
        )


    @tool
    def get_missing_values() -> str:
        """Return missing-value counts and percentages
        for columns that contain missing values.
        """

        missing = df.isnull().sum()

        result = []

        for column, count in missing.items():

            if count >0:

                percentage = (count/len(df)) * 100

                result.append(
                    f"{column}: "
                    f"{count} missing "
                    f"({percentage:.2f}%)"
                )
            if not result:
                return "No missing values were detected"

            return "\n".join(result)




    @tool

    def get_unique_values(column:str)->str:

        """
        Return unique value information for a column, including the number of unique values and
        the most frequent values.
        """
        if column not in df.columns:
            return f"Column '{column}' can not be found in the dataset."
        unique_values = df[column].nunique()


        top_values = (
                df[column]
            .value_counts(dropna=False)
            .head(10)
        )

        result = [
            f"Column: {column}",
            f"Unique values: {unique_values}",
            "",
            "Most frequent values:"
        ]
        for value, count in top_values.items():
            result.append(
                f"{value}: {count}"
             )
        return "\n".join(result)
    @tool
    def get_duplicated_values()->str:
        """
        Return the duplicated rows present in the dataset.
        """

        duplicated_rows = int(df.duplicated().sum())


        return (
            f"The dataset contains "
            f"{duplicated_rows} duplicate rows."
        )


    @tool
    def get_outliers()->str:
        """Detect potential numerical outliers using the IQR mehtod and return outlier counts"""

        results = detect_outliers(df)

        if not results:
            return "No numerical columns are available for outlier analsis."

        output = []

        for column, data in results.items():

            output.append(
                f"{column}: "
                f"{data['outlier_count']} outliers"
            )
        return "\n".join(output)


    @tool
    def get_correlations() -> str:

        """Return the correlation matrix for numerical columns."""

        correlations = correlation_analysis(df)


        if not correlations:
            return (
                "At least two numerical columns "
                "are required for correlation analysis."
            )

        output = []

        for column, values in correlations.items():
            for other_column, correlation in values.items():
                if column >= other_column:
                    continue

                output.append(
                    f"{column} <-> {other_column}: "
                    f"{correlation}:.4f"
                )
        return "\n".join(output)

    @tool
    def aggregate_by_category(
        category_column: str,
        value_column: str,
        operation: str = "sum",
    ) -> str:
        """Aggregate a numerical column by a categorical column.
        Supported operations are sum, mean, median, min and max."""

        if category_column not in df.columns:
            return (
                f"Column '{category_column}' "
                "does not exist."
            )

        if value_column not in df.columns:
            return (
                f"Column '{value_column}' "
                "does not exist."
            )

        if not pd.api.types.is_numeric_dtype(
            df[value_column]
        ):
            return (
                f"Column '{value_column}' "
                "is not numerical."
            )

        if operation not in {
            "sum",
            "mean",
            "median",
            "min",
            "max",
        }:
            return (
                "Unsupported operation. "
                "Use sum, mean, median, min or max."
            )

        grouped = (
            df.groupby(category_column)[value_column]
        )

        if operation == "sum":
            result = grouped.sum()

        elif operation == "mean":
            result = grouped.mean()

        elif operation == "median":
            result = grouped.median()

        elif operation == "min":
            result = grouped.min()

        else:
            result = grouped.max()

        output = []

        for category, value in result.items():

            output.append(
                f"{category}: {value:.2f}"
            )

        return "\n".join(output)

            




    return [
        get_dataset_info,
        get_column_info,
        get_column_statistics,
        get_duplicated_values,
        get_unique_values,
        get_correlations,
        get_outliers,
        aggregate_by_category
    ]