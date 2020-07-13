# Temper Utils
Tools for [Temper](https://github.com/floriaaan/temper/) app, using Python >= 3 (tested with 3.7)

SQL structure for Temper DB

## Utils

* [temper.sql](https://github.com/floriaaan/temper-utils/blob/master/temper.sql)

* [api-temperature.py](https://github.com/floriaaan/temper-utils/blob/master/api-temperature.py)
  * (venv) : requests, dotenv
  * Request measures from an external API : [OpenWeather API](https://openweathermap.org/api)

* [random-temperature.py](https://github.com/floriaaan/temper-utils/blob/master/random-temperature.py)
  * (venv) : requests
  * Generate random measures (between temp = [17 and 23], humid = [50 and 60])

* [cpu.py](https://github.com/floriaaan/temper-utils/blob/master/cpu.py) [WIP]
  * (venv) : requests, wmi
  * Get the CPU temperature
