import aiohttp
import asyncio

async def download_file(url: str, file_path: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(file_path, 'wb') as f:
                f.write(await response.read())

async def main():
    url = "https://pcoptimizedsettings.com/wp-content/uploads/2024/07/ZZZ_Poster_Official.jpeg"
    file_path = "image.png"
    await download_file(url, file_path)
    print("File downloaded.")

if __name__ == "__main__":
    asyncio.run(main())
