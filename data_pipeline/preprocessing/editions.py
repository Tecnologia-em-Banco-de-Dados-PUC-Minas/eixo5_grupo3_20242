import os
from datetime import datetime
import pandas as pd

from data_pipeline.constants import RAW_PATH, PREPROCESSED_PATH


def format_date(date, year):
    if pd.isna(date):
        return None
    
    try:
        return pd.to_datetime(date, format='%d %B %Y')
    except ValueError:
        date = f'{date} {year}'
        return pd.to_datetime(date, format='%d %B %Y')


def format_competition_start(date, competition_end):
    if pd.isna(date) or pd.isna(competition_end):
        return None

    try:
        date = pd.to_datetime(date, format='%d %B')
        return date.replace(year=competition_end.year)
    except ValueError:
        date = f'{date} {competition_end.month} {competition_end.year}'
        return pd.to_datetime(date, format='%d %m %Y')
    

def process_editions():
    df = pd.read_csv(f'{RAW_PATH}/editions.csv')

    # Remove Ancient Olympic Games
    df = df[~df['type'].isin(['Ancient Olympic Games'])]

    # Cast year column to numeric
    df['Year'] = pd.to_numeric(df['Year'])

    # Handle Opened and Closed informations, to correctly parse the dates
    df['Opened'] = df.apply(lambda row: format_date(row['Opened'], row['Year']), axis=1)
    df['Closed'] = df.apply(lambda row: format_date(row['Closed'], row['Year']), axis=1)

    # Split 'Competition' column into 'competition_start' and 'competition_end'
    df[['competition_start', 'competition_end']] = df['Competition'].str.split(' – ', expand=True)

    # Handle competitions dates, to correctly parse the dates
    df['competition_end'] = df.apply(lambda row: format_date(row['competition_end'], row['Year']), axis=1)
    df['competition_start'] = df.apply(lambda row: format_competition_start(row['competition_start'], row['competition_end']), axis=1)

    # Add war_related_cancellation column
    df['war_related_cancellation'] = df['Unnamed: 7'] == 'Not held due to war'

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Keep columns
    colums_to_keep = ['type', 'season', 'year', 'city', 'opened', 'closed',
                      'competition_start', 'competition_end', 'war_related_cancellation']
    df = df[colums_to_keep]

    # Define the directory and create it if it doesn't exist
    directory = f'{PREPROCESSED_PATH}/editions'
    os.makedirs(directory, exist_ok=True)

    # Write to parquet
    df.to_parquet(f'{directory}/parquet-data-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.parquet')


if __name__ == '__main__':
    process_editions()
