import pandas as pd


def process_athlete_bios():
    df = pd.read_csv('datalake/bronze/athlete_bios.csv')

    # Remove the "•" from the Used name
    df['name'] = df['Used name'].str.replace("•", " ")

    # Split the Measurements column into height & weight columns
    df[['height_cm', 'weight_kg']] = df['Measurements'].str.split('/', expand=True)

    # Get rid of " cm" and the " kg" from our new columns
    df['height_cm'] = pd.to_numeric(df['height_cm'].str.strip(' cm'), errors='coerce')
    df['weight_kg'] = pd.to_numeric(df['weight_kg'].str.strip(' kg'), errors='coerce')

    # Parse out dates from 'Born' and 'Died' columns
    date_pattern = r'(\d+ \w+ \d{4}|\d{4})'
    df['born_date'] = df['Born'].str.extract(date_pattern)
    df['born_year'] = df['Born'].str.extract(r'(\d{4})')

    df['born_date'] = pd.to_datetime(df['born_date'], format="mixed", errors='coerce')
    df['born_year'] = pd.to_numeric(df['born_year'])

    df['died_date'] = df['Died'].str.extract(date_pattern)
    df['died_year'] = df['Died'].str.extract(r'(\d{4})')

    df['died_date'] = pd.to_datetime(df['died_date'], format="mixed", errors='coerce')
    df['died_year'] = pd.to_numeric(df['died_year'])

    # Get city, region, and country from Born column
    location_pattern = r'in ([\w\s()-]+), ([\w\s-]+) \((\w+)\)'
    df[['born_city','born_region','born_country']] = df['Born'].str.extract(location_pattern, expand=True)

    location_pattern = r'in ([\w\s()-]+), ([\w\s-]+) \((\w+)\)'
    df[['died_city','died_region','died_country']] = df['Died'].str.extract(location_pattern, expand=True)

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Keep columns
    colums_to_keep = ['athlete_id', 'name', 'roles', 'sex', 'noc', 'height_cm', 'weight_kg',
                      'born_date', 'born_year', 'born_city', 'born_region', 'born_country',
                      'died_date', 'died_year', 'died_city', 'died_region', 'died_country']
    df = df[colums_to_keep]

    # Write to parquet
    df.to_parquet('datalake/silver/athlete_bios.parquet')


if __name__ == '__main__':
    process_athlete_bios()
