import requests
import pandas as pd
from bs4 import BeautifulSoup

from data_pipeline.constants import BASE_URL, RAW_PATH


def get_events():
    events_url = f'{BASE_URL}/event_names'

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

    events.to_csv(f'{RAW_PATH}/events.csv', index=False)


if __name__ == '__main__':
    get_events()
