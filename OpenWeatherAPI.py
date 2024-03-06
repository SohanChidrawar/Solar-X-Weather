import requests

# API Key obtained by Subscribing to OpenWeatherMap.org
# API used here is Personal and not intended to be shared or re-used by anyone other than the project leads

API_key = #'HIDDEN'

def current_weather_data(CITY, API):
    get_weather_details = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API}'
    weather_capture_raw = requests.get(get_weather_details)
    weather_data = weather_capture_raw.json()

    #print(weather_data)

    # Output ->
    # 'coord': {'lon': 73.8204, 'lat': 18.5741}

    # 'weather' - 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]

    # 'main': {'temp': 302.09, 'feels_like': 303.93, 'temp_min': 302.09, 'temp_max': 302.09,
    # 'pressure': 1009, 'humidity': 59, 'sea_level': 1009, 'grnd_level': 947}

    # 'visibility': 10000, 'wind': {'speed': 6.82, 'deg': 265, 'gust': 8.73}

    # ------------ Current Temperature --------------
    current_temp = int(weather_data['main']['temp'])

    # ------------ Feels Like Temperature --------------
    feels_like_temp = int(weather_data['main']['feels_like'])

    # ------------ Maximum Temperature --------------
    maximum_temp = int(weather_data['main']['temp_max'])

    # ------------ Minimum Temperature --------------
    minimum_temp = int(weather_data['main']['temp_min'])

    # ------------ Current Pressure --------------
    current_pressure = int(weather_data['main']['pressure'])

    # ------------ Current Humidity --------------
    current_humidity = int(weather_data['main']['humidity'])

    print("\nLocation: {}".format(CITY.upper()))
    print("Temperature: {}'C".format(round(current_temp-273.15, 1)))
    print("Feels like: {}'C".format(round(feels_like_temp-273.15, 1)))
    print("Maximum Temperature: {}'C".format(round(maximum_temp-273.15, 1)))
    print("Minimum Temperature: {}'C".format(round(minimum_temp-273.15, 1)))
    print("Pressure: {} Pa".format(current_pressure))
    print("Humidity: {} g/kg".format(current_humidity))


'''def coordinates_finder(CITY, API):
    limit = 5
    get_lat_long = f'http://api.openweathermap.org/geo/1.0/direct?q={CITY}&limit={limit}&appid={API}'
    lat_long_raw = requests.get(get_lat_long)
    lat_long_data = lat_long_raw.json()

    print(lat_long_data[1])'''

city = 'juni sangvi'#input("Enter City name: ")

current_weather_data(city, API_key)
