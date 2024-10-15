import asyncio

async def main() -> None:
    a, b = 0, 1
    for i in range (1, 11):
        print(a)
        a, b = b, a + b
        await asyncio.sleep(1)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
