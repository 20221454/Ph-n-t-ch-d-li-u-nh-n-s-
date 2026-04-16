import pandas as pd
import os

def load_data():
    base_path = os.path.dirname(__file__)

    file_path = os.path.join(
        base_path,
        "..",
        "data",
        "dataset_cleaned.csv"
    )

    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    return df