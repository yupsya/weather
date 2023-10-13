
from requests import get


def get_weather(city):
    r = get(f'http://127.0.0.1:8000/weather?city={city}')
    print(r.json())
    return r.json()