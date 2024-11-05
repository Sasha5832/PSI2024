import aiohttp
import asyncio

async def fetch_url(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_weather_for_cities(cities: dict) -> dict:
    async def fetch_city_weather(city: str, lat: float, lon: float) -> dict:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&hourly=temperature_2m"
        return {city: await fetch_url(url)}

    tasks = [fetch_city_weather(city, lat, lon) for city, (lat, lon) in cities.items()]
    results = await asyncio.gather(*tasks)
    return {k: v for result in results for k, v in result.items()}

async def main():
    cities = {
        "Porlamar": (10.95, -63.87),
        "Moroni": (-11.70, 43.25),
        "Helsinki": (60.17, 24.94)
    }
    weather = await fetch_weather_for_cities(cities)
    print(weather)

if __name__ == "__main__":
    asyncio.run(main())
