from flask import Flask, request
from flask_cors import CORS
from flask import jsonify
import json
import logging
from db import get_user_embedding, user_login, set_user_embedding

from service import microservice_for_rec
from predict_parameter import Hyper_parameters
from pathlib import Path
import random


args = Hyper_parameters()
mapper = {}

with open(Path(args.test_file[0]), "r") as reader:
    mapper["restaurant"] = json.loads(reader.read())

with open(Path(args.test_file[1]), "r") as reader:
    mapper["user"] = json.loads(reader.read())

with open(Path(args.test_file[2]), "r") as reader:
    mapper["test"] = json.loads(reader.read())

service = microservice_for_rec("model.pkg")

restIds = random.sample(range(len(mapper["test"])), 50)
rest_embeddings = []

for id in restIds:
    rest_embeddings.append(
        (id, service.GetRestaurantRepresentation(mapper["restaurant"][mapper["test"][id]["restaurant"]]))
    )


logging.basicConfig(filename="app.log", level=logging.INFO)

app = Flask("app")
CORS(app)

user_id = -1
user_embedding = None


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/login", methods=["POST"])
def login():
    r = json.loads(request.data)
    global user_id

    user_id = r["userId"]
    if user_login(user_id) == "login success":
        result = {"message": "success", "content": str(user_id) + "login successfully"}
    else:
        result = {"message": "error", "content": str(user_id) + "login Failed"}
    logging.info(user_id)
    return result


@app.route("/compute_user_embedding")
def compute_user_embedding():
    global user_embedding
    review = request.args.get("review")
    logging.warning("review: " + str(review))
    vector = service.GetUserRepresentation(str(review))
    user_embedding = vector
    # set_user_embedding(user_id, vector.tolist())
    return {"message": "success", "content": "Compute vector success"}


@app.route("/predict")
def predict():
    global user_id
    # user_embedding_obj = get_user_embedding(user_id)
    # user_embedding = user_embedding_obj["user_embedding"]
    global user_embedding

    logging.info("user_embedding: " + str(user_embedding))
    if user_embedding != "default":
        result = []
        for id, embedding in rest_embeddings:
            score = service.RecommendRestaurant(user_embedding, embedding).tolist()[0]
            result.append((id, score))
        result = sorted(result, key=lambda x: x[1])
        logging.warning(result)
        return {"message": "success", "content": "predict success", "res": result[:3]}
    else:
        return {"message": "error", "content": "User vector does not exist!"}


app.run(port=4000, debug=True)
