from flask import Flask, send_file, request
from flask import json

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("templates/index.html")

@app.route("/train", methods=['POST'])
def train():
    data = json.loads(request.data.decode())
    id = data["roadId"]
    return id


if __name__ == "__main__":
    app.run()
