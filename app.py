from quart import Quart, jsonify

from data_async import gd, response2

app = Quart(__name__)


@app.route("/")
async def get_data():
    return await gd(1)


@app.route("/max")
async def get_max():
    # return jsonify({"max": max(await response1())})
    return jsonify({"max": max(await response2())})
    # return jsonify({"max": max(await response3())})


if __name__ == "__main__":
    app.run(debug=True)
