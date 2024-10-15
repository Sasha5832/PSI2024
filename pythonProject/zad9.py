import asyncio

async def maszyna_a():
    for a in range(7):
        await asyncio.sleep(2)
        print("Maszyna A Działą")

async def maszyna_b():
    for b in range(5):
        await asyncio.sleep(3)
        print("Maszyna B Działą")

async def maszyna_c():
    for c in range(3):
        await asyncio.sleep(5)
        print("Maszyna C Działą")

async def main() -> None:
    await asyncio.gather(maszyna_a(), maszyna_b(), maszyna_c())

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
