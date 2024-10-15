import asyncio

async def wczytanie(pliknr):
    await asyncio.sleep(2)
    print(f"Wczytanie pliku {pliknr}")

async def analiza(pliknr):
    await asyncio.sleep(1)
    print(f"Fnaliza pliku {pliknr}")

async def zapis(pliknr):
    await asyncio.sleep(1)
    print(f"Zapis pliku {pliknr}")

async def plik(pliknr):
    await wczytanie(pliknr)
    await analiza(pliknr)
    await zapis(pliknr)

async def main() -> None:
    await asyncio.gather(*(plik(i) for i in range(1, 6)))

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
