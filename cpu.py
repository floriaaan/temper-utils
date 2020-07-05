import requests
import random
import json

import wmi



def http_post(probe_id, temp, humidity):
    url = 'http://localhost:5000/temper/api/v1/measure/'
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
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        print(temperature_infos)
        probe = 1
        #http_post(probe, temp, humid)
        print("POST: Sonde:"+ str(probe))
        time.sleep(1000)
    except Exception as e:
        print(str(e))