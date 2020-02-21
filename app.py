from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/index')
def index():
    response = dict(
        message = "Hello World"
    )
    print(response)
    return jsonify(response),200

@app.route('/item')
def listItem():
    return jsonify({
        "message": "This is Item"
    }), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
