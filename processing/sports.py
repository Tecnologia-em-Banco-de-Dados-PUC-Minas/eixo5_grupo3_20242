import pandas as pd
    

def process_sports():
    df = pd.read_csv('datalake/bronze/sports.csv')

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Keep columns
    colums_to_keep = ['abbreviation', 'discipline', 'sport', 'season']
    df = df[colums_to_keep]

    # Write to parquet
    df.to_parquet('datalake/silver/sports.parquet')


if __name__ == '__main__':
    process_sports()
