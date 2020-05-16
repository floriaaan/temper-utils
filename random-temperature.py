import requests
import random
import json
import time

def http_post(probe_id, temp, humidity):
    url = 'http://floriaaan.alwaysdata.net/temper/api/v1/measure/'
    data = {
        'probe' : probe_id,
        'temperature' : temp,
        'humidity' : humidity
    }
    headers = {
        'charset': 'utf-8'
    }
    resp = requests.post(url, json=data, headers=headers)

while True:
    try:
        temp = random.randint(17, 23)
        humid = random.randint(50, 60)
        probe = 1
        http_post(probe, temp, humid)
        print("POST: Sonde:"+ str(probe) + " + Temp :" + str(temp) + ' + Humid : ' + str(humid))
    except KeyboardInterrupt:
        exit()
    except:
        print("!!!ERROR!!!")

    time.sleep(3)