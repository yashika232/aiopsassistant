import os
import requests
import time

def get_weather(city: str, retries: int = 2):
    for attempt in range(retries):
        try:
            response = requests.get(
                "http://api.weatherapi.com/v1/current.json",
                params={
                    "key": os.getenv("WEATHERAPI_KEY"),
                    "q": city,
                    "aqi": "no"
                }
            )
            response.raise_for_status()
            data = response.json()

            return {
                "city": city,
                "temperature_c": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"]
            }

        except Exception as e:
            if attempt == retries - 1:
                return {"error": str(e)}
            time.sleep(1)
