import os
from datetime import datetime
import pandas as pd
    

def process_noc_regions():
    df = pd.read_csv('datalake/bronze/noc_regions.csv')

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Define the directory and create it if it doesn't exist
    directory = 'datalake/silver/noc_regions'
    os.makedirs(directory, exist_ok=True)

    # Write to parquet
    df.to_parquet(f'{directory}/parquet-data-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.parquet')


if __name__ == '__main__':
    process_noc_regions()
