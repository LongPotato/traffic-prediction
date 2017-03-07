from flask import Flask, send_file, request
from flask import json

from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

app = Flask(__name__)

input = [[10, 0, 1, 8], [10, 0, 2, 9], [10, 1, 1, 13], [5, 0, 1, 15], [5, 1, 5, 16], [5, 1, 6, 18]]
output = [8, 7, 5, 6, 9, 9]

@app.route("/")
def index():
    return send_file("templates/index.html")

@app.route("/train", methods=['POST'])
def train():
    data = json.loads(request.data.decode())
    id = data["roadId"]

    input.append([int(data["roadId"]), int(data["direction"]),int(data["day"]),int(data["time"]) ])
    output.extend([int(data["traffic"])])


    return id


@app.route("/predict", methods=['POST'])
def predict():
    data = json.loads(request.data.decode())
    id = data["roadId"]


    model = make_pipeline(PolynomialFeatures(2), Ridge())
    model.fit(input, output)
    preData = [int(data["roadId"]), int(data["direction"]), int(data["day"]), int(data["time"])]
    print (preData)
    model.predict([preData])



    return (model.predict([preData]))


if __name__ == "__main__":
    app.run()
