from typing import Dict

import pandas as pd

datasets: Dict[str, pd.DataFrame] = {}

def save_dataset(
        dataset_id:str,
        df:pd.DataFrame,
)-> None:
    datasets[dataset_id] = df

def get_dataset(
    dataset_id:str,
    
)-> pd.DataFrame | None:
    return datasets.get(dataset_id)
