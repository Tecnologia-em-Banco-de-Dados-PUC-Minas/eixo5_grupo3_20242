import os
from datetime import datetime
import pandas as pd

from data_pipeline.constants import RAW_PATH, PREPROCESSED_PATH


def process_athlete_results():
    df = pd.read_csv(f'{RAW_PATH}/athlete_results.csv', dtype={'Nationality': str})

    # Get place column
    df['place'] = df['Pos'].str.extract(r'(\d+)')
    df['place'] = pd.to_numeric(df['place'])

    # Separate Games column into year, season and youth_event
    df[['year', 'season', 'youth_event']] = df['Games'].str.extract(r'(\d{4}) (Summer|Winter|Equestrian|Intercalated)(?: (Youth))?', expand=True)
    df['year'] = pd.to_numeric(df['year'])
    df['youth_event'] = df['youth_event'] == 'Youth'

    # Rename columns
    df.rename(columns={'As': 'name'}, inplace=True)

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Keep columns
    colums_to_keep = ['athlete_id', 'name', 'noc', 'nationality', 'place', 'medal',
                    'year', 'season', 'discipline', 'event', 'team', 'youth_event']
    df = df[colums_to_keep]

    # Define the directory and create it if it doesn't exist
    directory = f'{PREPROCESSED_PATH}/athlete_results'
    os.makedirs(directory, exist_ok=True)

    # Write to parquet
    df.to_parquet(f'{directory}/parquet-data-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.parquet')


if __name__ == '__main__':
    process_athlete_results()
