import asyncio


async def demo():
    print("Hello")
    await asyncio.sleep(1)
    print("world")


asyncio.run(demo())
