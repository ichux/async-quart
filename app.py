from asyncio import create_task

from quart import Quart, jsonify

from data_async import gd, stl

app = Quart(__name__)


@app.route("/")
async def get_data():
    return await gd(1)


@app.route("/max")
async def get_max():
    # return jsonify({"data": max([await stl(0), await stl(1), await stl(2), await stl(3), await stl(4)])})
    return jsonify(
        {
            "max": max(
                [await future for future in [create_task(stl(_)) for _ in range(5)]]
            )
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
