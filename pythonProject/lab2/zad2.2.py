import aiohttp
import asyncio

async def fetch(url: str, header: dict, body: dict) -> dict:
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.post(url, data=body) as response:
            return await response.json()


async def main() -> None:
    url = "https://jsonplaceholder.typicode.com/posts"
    header = {"Authorizatiom": "Bearer SOME_CHARS"}
    body = {"key": "value"}
    response = await fetch(url, header, body)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
