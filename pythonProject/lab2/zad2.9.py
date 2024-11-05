import aiohttp
import asyncio

async def fetch_with_retries(url: str, retries: int = 3) -> dict:
    async with aiohttp.ClientSession() as session:
        for attempt in range(retries):
            try:
                async with session.get(url) as response:
                    if 200 <= response.status < 300:
                        return await response.json()
                    elif 500 <= response.status < 600:
                        continue
            except aiohttp.ClientError:
                if attempt == retries - 1:
                    return {"error": "Failed after retries."}
    return {}

async def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    responses = await asyncio.gather(*[fetch_with_retries(url) for _ in range(100)])
    successful_responses = [resp for resp in responses if isinstance(resp, dict) and 'error' not in resp]
    print(f"Successful responses: {len(successful_responses)}")

if __name__ == "__main__":
    asyncio.run(main())
