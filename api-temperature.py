import requests
import random
import json
import time

from dotenv import load_dotenv
load_dotenv()
import os

def http_get(url):
    response = requests.get(url)
    if(response.status_code == 200):
        return response.json()
    else:
        return False

def http_post(probe_id, temp, humidity):
    url = 'http://localhost:8000/api/v1/measure/'
    data = {
        'probe' : probe_id,
        'temperature' : temp,
        'humidity' : humidity
    }
    headers = {
        'charset': 'utf-8'
    }
    resp = requests.post(url, json=data, headers=headers)
    print(resp.text)

while True:
    try:
        response = http_get("http://api.openweathermap.org/data/2.5/weather?q=Rouen&appid=" + os.getenv('OWEATHER_API_KEY'))
        probe = 2
        temp = response['main']['temp'] - 273.15
        humid = response['main']['humidity']
        http_post(probe, temp, humid)
    except KeyboardInterrupt:
        exit() 
    except Exception as e:
        print("!!!ERROR!!! - %s" % str(e))
    time.sleep(20)