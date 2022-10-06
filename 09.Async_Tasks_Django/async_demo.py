import asyncio
import time


async def first_worker():
    await asyncio.sleep(2)
    return "bread"


async def second_worker():
    await asyncio.sleep(3)
    return "cheese"


async def third_worker():
    await asyncio.sleep(4)
    return "ham"


async def main():
    start = time.time()

    result = await asyncio.gather(first_worker(), second_worker(), third_worker())

    # When the above is ready, the following executes
    end = time.time()
    total_time = start - end
    print(f"Executed in : {total_time}")
    print(result)

asyncio.run(main())
"""
All operations simultaneously 
"""
