import pandas as pd
    

def process_events():
    df = pd.read_csv('datalake/bronze/events.csv')

    # Get rid of the "(discontinued)" from the Event column
    df['discontinued'] = df['Event'].str.extract(r'\(([^)]+)\)$')
    df['Event'] = df['Event'].str.replace(r' \([^)]+\)$', '', regex=True) 
    df['discontinued'] = df['discontinued'] == 'discontinued'

    # Get rid of the "(non-medal only)" from the Discipline column
    df['non_medal'] = df['Discipline'].str.extract(r'\(([^)]+)\)$')
    df['Discipline'] = df['Discipline'].str.replace(r' \([^)]+\)$', '', regex=True) 
    df['non_medal'] = df['non_medal'] == 'non-medal only'

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Write to parquet
    df.to_parquet('datalake/silver/events.parquet')


if __name__ == '__main__':
    process_events()
