import requests
from datetime import datetime
from pytz import timezone

URL_API = 'https://devman.org/api/challenges/solution_attempts/'
START_NIGHT_HOUR = 0
STOP_NIGHT_HOUR = 6


def load_attempts():
    responce = requests.get(URL_API)
    pages_count = responce.json()['number_of_pages']
    start_page = responce.json()['page']
    yield from responce.json()['records']
    for page_number in range(start_page+1, pages_count+1):
        params = {
              'page': page_number
        }
        responce = requests.get(URL_API, params=params)
        yield from responce.json()['records']


def get_midnighters():
    for attempt in load_attempts():
        user_timezone = timezone(attempt['timezone'])
        user_time_stamp = datetime.fromtimestamp(attempt['timestamp'])
        user_time = user_timezone.localize(user_time_stamp)
        if START_NIGHT_HOUR <= user_time.hour < STOP_NIGHT_HOUR:
            yield attempt['username']


def main():
    midnighters = set(get_midnighters())
    print("Всего сов: ", len(midnighters))
    print("А именно:")
    for midnighter in midnighters:
        print(midnighter)

if __name__ == '__main__':
    main()
