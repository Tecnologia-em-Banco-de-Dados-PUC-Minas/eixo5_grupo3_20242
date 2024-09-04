import pandas as pd


def process_athlete_results():
    df = pd.read_csv('datalake/bronze/athlete_results.csv', dtype={'Nationality': str})

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

    # Write to parquet
    df.to_parquet('datalake/silver/athlete_results.parquet')


if __name__ == '__main__':
    process_athlete_results()
