import asyncio


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
