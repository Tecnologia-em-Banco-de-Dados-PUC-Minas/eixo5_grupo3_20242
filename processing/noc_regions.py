import pandas as pd
    

def process_noc_regions():
    df = pd.read_csv('datalake/bronze/noc_regions.csv')

    # Put snake_case on columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Write to parquet
    df.to_parquet('datalake/silver/noc_regions.parquet')


if __name__ == '__main__':
    process_noc_regions()
