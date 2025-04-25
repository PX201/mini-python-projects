import requests
import os
from dotenv import load_dotenv

#Load the API key from .env
load_dotenv()

class Weather:
    def __init__(self):
        self.API_KEY = os.getenv("OPENWEATHER_API_KEY")

    def get_weather(self,city):
            uri = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.API_KEY}&units=metric"
            response = requests.get(uri)

            if response.status_code == 200:
                data = response.json()
                print("#"*30)
                print(f" Weather in {data['name']}, {data['sys']['country']}")
                print(f"Temperature: {data['main']['temp']}C")
                print(f"Condition: {data['weather'][0]['description']}")
                print("#"*30)
            else:
                print("Error fetching weather data. Please check the city name")
