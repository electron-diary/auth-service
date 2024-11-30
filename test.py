import asyncio

async def first():
    await asyncio.sleep(1)
    print("first")

async def second():
    await asyncio.sleep(3)
    print("second")


async def main():
    await asyncio.gather(second(), first())

if __name__ == "__main__":
    asyncio.run(main())