import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

from data_pipeline.constants import BASE_URL, RAW_PATH


def get_sports():
    sports_url = f'{BASE_URL}/sports'
    
    try:
        response = requests.get(sports_url, timeout=60)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            table = soup.find('table')
            sports = pd.read_html(StringIO(str(table)))[0]

        else:
            print(f'Failed to retrieve the {sports_url} webpage. Status code:', response.status_code)

    except Exception as e:
        print(e)

    sports.to_csv(f'{RAW_PATH}/sports.csv', index=False)


if __name__ == '__main__':
    get_sports()
