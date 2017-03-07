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
    ## put this when predicting with the input
#    model = make_pipeline(PolynomialFeatures(2), Ridge())
 #   model.fit(input, output)


    return id


@app.route("/predict", methods=['POST'])
def train():
    data = json.loads(request.data.decode())
    id = data["roadId"]
    return id;


if __name__ == "__main__":
    app.run()
