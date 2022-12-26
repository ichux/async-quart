import asyncio
from asyncio import create_task

from quart import Quart, jsonify

from data_async import gd, stl

app = Quart(__name__)


@app.route("/")
async def get_data():
    return await gd(1)


async def response1():
    return [await stl(0), await stl(1), await stl(2), await stl(3), await stl(4)]


async def response2():
    # return await asyncio.gather(*[stl(0), stl(1), stl(2), stl(3), stl(4)])
    return await asyncio.gather(*[stl(_) for _ in range(5)])


async def response3():
    return [await future for future in [create_task(stl(_)) for _ in range(5)]]


@app.route("/max")
async def get_max():
    # return jsonify({"max": max(await response1())})
    return jsonify({"max": max(await response2())})
    # return jsonify({"max": max(await response3())})


if __name__ == "__main__":
    app.run(debug=True)
