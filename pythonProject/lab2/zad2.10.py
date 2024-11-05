import aiohttp
import asyncio

async def fetch_url_as_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def process_data(data: dict) -> str:
    # Przetwarzanie danych, np. konwersja do stringa
    return f"Processed {data}"

async def save_to_file(data: str, file_path: str) -> None:
    with open(file_path, 'a') as f:
        f.write(data + "\n")

async def fetch_and_process(url: str, file_path: str) -> None:
    data = await fetch_url_as_json(url)  # Używamy funkcji z zadania 4
    processed = await process_data(data)
    await save_to_file(processed, file_path)

async def main():
    url = "https://jsonplaceholder.typicode.com/posts"  # Możesz zmienić na inne API
    file_path = "output.txt"
    await fetch_and_process(url, file_path)
    print("Data processed and saved.")

if __name__ == "__main__":
    asyncio.run(main())
