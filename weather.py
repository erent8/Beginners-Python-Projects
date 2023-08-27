import requests
import datetime

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"

CITY_NAME = input("Enter the city name...")

URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY_NAME

response = requests.get(URL)
data = response.json()

def wind_direction(degrees):
    if 337.5 <= degrees < 22.5:
        return "North"
    elif 22.5 <= degrees < 67.5:
        return "Northeast"
    elif 67.5 <= degrees < 112.5:
        return "East"
    elif 112.5 <= degrees < 157.5:
        return "Southeast"
    elif 157.5 <= degrees < 202.5:
        return "South"
    elif 202.5 <= degrees < 247.5:
        return "Southwest"
    elif 247.5 <= degrees < 292.5:
        return "West"
    else:
        return "Northwest"

if data['cod'] != "404":
    forecasts = data["list"]  # List of weather forecasts

    for forecast in forecasts:
        timestamp = forecast["dt"]
        temp_kelvin = forecast["main"]["temp"]
        temp_min = forecast["main"]["temp_min"]
        temp_max = forecast["main"]["temp_max"]
        humidity = forecast["main"]["humidity"]
        wind_speed = forecast["wind"]["speed"]
        wind_direction_deg = forecast["wind"]["deg"]
        clouds = forecast["clouds"]["all"]
        rain = forecast.get("rain", {}).get("3h", 0)
        snow = forecast.get("snow", {}).get("3h", 0)
        visibility = forecast["visibility"]
        uv_index = forecast.get("uv", 0)
        description = forecast["weather"][0]["description"]
        pressure = forecast["main"]["pressure"]
        country = data["city"]["country"]

        date_time = datetime.datetime.fromtimestamp(timestamp)
        day_of_week = date_time.strftime("%A")
        formatted_date_time = date_time.strftime("%d/%m/%Y %H:%M")

        temp_celsius = temp_kelvin - 273.15
        temp_celsius_min = temp_min - 273.15
        temp_celsius_max = temp_max - 273.15

        wind_dir = wind_direction(wind_direction_deg)

        print("Date and Time:", formatted_date_time)
        print("Day:", day_of_week)
        print("Temperature: {:.2f} °C".format(temp_celsius))
        print("Min Temperature: {:.2f} °C".format(temp_celsius_min))
        print("Max Temperature: {:.2f} °C".format(temp_celsius_max))
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "m/s")
        print("Wind Direction:", wind_dir)
        print("Cloud Cover:", clouds, "%")
        print("Rain (3h):", rain, "mm")
        print("Snow (3h):", snow, "mm")
        print("Visibility:", visibility, "meters")
        print("UV Index:", uv_index)
        print("Weather Description:", description)
        print("Pressure:", pressure, "hPa")
        print("Country:", country)
        print("------------------------")

else:
    print("Invalid city name...")
