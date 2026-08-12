from langchain.tools import tool
from app.services.dataset_store import get_dataset

# we are trying to create the structure that every single dataset will have their own tool
# Dataset A
#    ↓
# Tools A

# Dataset B
#    ↓
# Tools B

def create_dataset_tools(dataset_id:str):

    @tool
    def get_column_average(column:str)->str:
        """calculate the average value of a numerical column."""

        df = get_dataset(dataset_id)

        if df is None:
            return "Dataset not found"
        if column not in df.columns:
            return f"Column '{column}' does not exist"
        if not df[column].dtype.kind in "biufc":
            return f"Column '{column}' is not numerical"

        value = df[column].mean()

        return f"The average of {column} is {value:.2f}"

    return [
        get_column_average,
    ]