import aiohttp
import asyncio

async def fetch_url_as_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_weather() -> dict:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.2969&longitude=20.0364&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    return await fetch_url_as_json(url)

async def main():
    weather = await fetch_weather()
    print(weather)

if __name__ == "__main__":
    asyncio.run(main())
