import asyncio
from asyncio import create_task


async def gd(ttl):
    await asyncio.sleep(ttl)
    return "Done!"


async def stl(hl: int):
    await asyncio.sleep(hl)
    return hl


def nap(hl: int):
    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(asyncio.sleep(hl))
    finally:
        loop.close()


def f1(a=None):
    nap(1)
    return a


def g1(a=None):
    nap(2)
    return a


async def response1():
    return [await stl(0), await stl(1), await stl(2), await stl(3), await stl(4)]


async def response2():
    # return await asyncio.gather(*[stl(0), stl(1), stl(2), stl(3), stl(4)])
    return await asyncio.gather(*[stl(_) for _ in range(5)])


async def response3():
    return [await future for future in [create_task(stl(_)) for _ in range(5)]]
