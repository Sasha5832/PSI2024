import aiohttp
import asyncio


async def fetch_city_weather(city: str, lat: float, lon: float) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=wind_speed_10m,temperature_2m"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return {city: await response.json()}  # Zwraca JSON dla miasta


async def fetch_filtered_weather(cities: dict, filters: dict) -> dict:
    async def city_weather_filter(city: str, lat: float, lon: float) -> dict:
        data = await fetch_city_weather(city, lat, lon)
        weather_data = data[city].get("hourly", {})

        # Filtrujemy na podstawie prognoz i maski
        for key, max_value in filters.items():
            hourly_data = weather_data.get(key, [])
            if hourly_data and all(value < max_value for value in hourly_data):
                return {city: weather_data}  # Dodajemy miasto, jeśli spełnia kryteria

        return {}

    tasks = [city_weather_filter(city, lat, lon) for city, (lat, lon) in cities.items()]
    results = await asyncio.gather(*tasks)
    return {k: v for result in results for k, v in result.items() if v}  # Usuwamy puste wyniki


async def main():
    cities = {
        "Porlamar": (10.95, -63.87),
        "Moroni": (-11.70, 43.25),
        "Helsinki": (60.17, 24.94)
    }
    filters = {"wind_speed_10m": 20}  # Przykład maski filtrowania
    filtered_weather = await fetch_filtered_weather(cities, filters)
    print(filtered_weather)


if __name__ == "__main__":
    asyncio.run(main())
