import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO


def get_sports():
    sports_url = 'https://www.olympedia.org/sports'
    
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

    sports.to_csv('datalake/bronze/sports.csv', index=False)


def get_events():
    events_url = 'https://www.olympedia.org/event_names'

    try:
        response = requests.get(events_url, timeout=60)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', {'class': 'table'})

            discipline = []
            events = []

            for row in table.find_all('tr'):
                discipline_tag = row.find('h2')
                if discipline_tag:
                    current_discipline = discipline_tag.text.strip().replace('\n', ' ')
                else:
                    event_tag = row.find('td')
                    if event_tag and current_discipline:
                        event_name = event_tag.text.strip().replace('\n', ' ')
                        discipline.append(current_discipline)
                        events.append(event_name)

            events = pd.DataFrame({
                'Discipline': discipline,
                'Event': events
            })

        else:
            print(f'Failed to retrieve the {events_url} webpage. Status code:', response.status_code)

    except Exception as e:
        print(e)

    events.to_csv('datalake/bronze/events.csv', index=False)


if __name__ == '__main__':
    get_sports()
    get_events()
