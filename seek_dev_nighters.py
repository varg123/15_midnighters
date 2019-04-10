import requests
from datetime import datetime
from pytz import timezone

URL_API = 'https://devman.org/api/challenges/solution_attempts/'
START_NIGHT_HOUR = 0
STOP_NIGHT_HOUR = 6


def load_attempts():
    current_page = 1
    end_page = 1
    while current_page <= end_page:
        params = {
              'page': current_page
        }
        attempts = requests.get(URL_API, params=params).json()
        end_page = attempts['number_of_pages']
        current_page += 1
        yield from attempts['records']


def get_midnighters():
    for attempt in load_attempts():
        user_timezone = timezone(attempt['timezone'])
        user_time = datetime.fromtimestamp(attempt['timestamp'], user_timezone)
        if START_NIGHT_HOUR <= user_time.hour < STOP_NIGHT_HOUR:
            yield attempt['username']


def main():
    midnighters = set(get_midnighters())
    print('Всего сов: ', len(midnighters))
    print('А именно:')
    for midnighter in midnighters:
        print(midnighter)

if __name__ == '__main__':
    main()
