import aiohttp
import asyncio

async def fetch_url(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_multiple_urls(urls: list) -> list:
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)

async def main() -> None:
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://reqres.in/api/users",
        "https://dog.ceo/api/breeds/image/random",
        "https://www.youtube.com",
        "https://www.youtube.com",
    ]
    contents = await fetch_multiple_urls(urls)
    for content in contents:
        print(content)

if __name__ == "__main__":
    asyncio.run(main())
