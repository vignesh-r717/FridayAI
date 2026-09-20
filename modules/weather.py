import requests

def get_weather(city="Coimbatore"):

    cities = {
        "coimbatore": (11.0168, 76.9558),
        "chennai": (13.0827, 80.2707),
        "bangalore": (12.9716, 77.5946),
        "mumbai": (19.0760, 72.8777),
        "delhi": (28.6139, 77.2090),
        "hyderabad": (17.3850, 78.4867),
    }

    city = city.lower()

    if city not in cities:
        return f"Sorry, I don't know the weather for {city.title()}."

    lat, lon = cities[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,weather_code,wind_speed_10m"
        f"&daily=precipitation_probability_max"
        f"&forecast_days=1"
    )

    try:

        data = requests.get(url, timeout=5).json()

        current = data["current"]
        daily = data["daily"]

        temp = current["temperature_2m"]
        wind = current["wind_speed_10m"]
        rain = daily["precipitation_probability_max"][0]

        report = (
            f"The current temperature in {city.title()} is {temp}°C. "
            f"Wind speed is {wind} km/h. "
            f"There is a {rain}% chance of rain today."
        )

        return report

    except Exception:
        return "Sorry, I couldn't fetch the weather."