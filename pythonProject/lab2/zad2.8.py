import aiohttp
import asyncio

async def fetch_weather_for_cities(cities: dict) -> dict:
    async def fetch_city_weather(city: str, lat: float, lon: float) -> dict:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return {city: await response.json()}

    tasks = [fetch_city_weather(city, lat, lon) for city, (lat, lon) in cities.items()]
    results = await asyncio.gather(*tasks)
    return {k: v for result in results for k, v in result.items()}


async def main():
    cities = {
        "Porlamar": (10.95, -63.87),
        "Moroni": (-11.70, 43.25),
        "Helsinki": (60.17, 24.94)
    }
    weather_data = await fetch_weather_for_cities(cities)

    # Obliczamy średnią temperaturę
    average_temperatures = {}
    for city, data in weather_data.items():
        hourly_temps = data["hourly"]["temperature_2m"]
        average_temp = sum(hourly_temps) / len(hourly_temps)
        average_temperatures[city] = average_temp

    # Sortowanie według średniej temperatury
    sorted_weather = dict(sorted(average_temperatures.items(), key=lambda item: item[1], reverse=True))
    print(sorted_weather)


if __name__ == "__main__":
    asyncio.run(main())
