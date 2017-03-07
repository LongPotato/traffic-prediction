from flask import Flask, send_file, request
from flask import json

from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

app = Flask(__name__)

input = []
output = []

@app.route("/")
def index():
    return send_file("templates/index.html")

@app.route("/train", methods=['POST'])
def train():
    data = json.loads(request.data.decode())
    id = data["roadId"]

    input.append([data["roadId"], data["direction"],data["day"],data["time"]])
    output.extend(data["traffic"])


    return id


@app.route("/predict", methods=['POST'])
def predict():
    data = json.loads(request.data.decode())
    id = data["roadId"]


    model = make_pipeline(PolynomialFeatures(2), Ridge())
    model.fit(input, output)

    prediction = model.predict([[data["roadId"],data["direction"], data["day"], data["time"]]])


    return prediction;


if __name__ == "__main__":
    app.run()
