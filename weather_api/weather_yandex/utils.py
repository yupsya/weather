from requests import get

from .models import Weather


def request_weather(location, key):
    res = get(url=f'http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no')
    res_dict = {
        'city': res.json()["location"]["name"],
        'temperature': res.json()["current"]["temp_c"],
        'pressure': res.json()["current"]["pressure_mb"],
        'wind_vel': res.json()["current"]["wind_kph"],
        'timestamp': res.json()["current"]["last_updated"],
    }
    return res_dict


def create_model(input_hashmap):
    model = Weather.objects.create(
        city=input_hashmap["city"],
        temperature=input_hashmap["temperature"],
        pressure=input_hashmap["pressure"],
        wind_vel=input_hashmap["wind_vel"],
        timestamp=input_hashmap["timestamp"]
    )
    return model


def strtoi_minutes(obj):
    string = str(obj)[14:16]
    return int(string)
