import asyncio

async def krojenie():
    await asyncio.sleep(2)
    print("krojenie")

async def gotowanie():
    await asyncio.sleep(5)
    print("gotowanie")

async def smażenie():
    await asyncio.sleep(3)
    print("smażenie")

async def main() -> None:
    await asyncio.gather(krojenie(), gotowanie(), smażenie())

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
