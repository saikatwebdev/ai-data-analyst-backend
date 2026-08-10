import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def create_correlation_heatmap(
        df: pd.DataFrame,
        output_path: str,

) -> None:

    numerical_df = df.select_dtypes(
        include="number"
    )

    if numerical_df.shape[1]<2:
        return

    correlation_matrix = numerical_df.corr()

    plt.figure(figsize=(10,8))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()