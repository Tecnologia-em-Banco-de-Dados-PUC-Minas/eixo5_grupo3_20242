import os
from datetime import datetime
import pandas as pd

from data_pipeline.constants import RAW_PATH, PREPROCESSED_PATH
    

def process_sports():
    df = pd.read_csv(f'{RAW_PATH}/sports.csv')

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Keep columns
    colums_to_keep = ['abbreviation', 'discipline', 'sport', 'season']
    df = df[colums_to_keep]

    # Define the directory and create it if it doesn't exist
    directory = f'{PREPROCESSED_PATH}/sports'
    os.makedirs(directory, exist_ok=True)

    # Write to parquet
    df.to_parquet(f'{directory}/parquet-data-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.parquet')


if __name__ == '__main__':
    process_sports()
