import asyncio

async def fetch(delay: int):
    await asyncio.sleep(delay)
    print(f"{delay}seconds")

async def main() -> None:
    await asyncio.gather(fetch(2), fetch(4), fetch(1))


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
