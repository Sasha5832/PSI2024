import asyncio

async def cor1():
    await asyncio.sleep(3)
    print("3s")

async def cor2():
    await asyncio.sleep(1)
    print("1s")

async def main() -> None:
    await asyncio.gather(cor1(), cor2())

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
