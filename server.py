from flask import Flask, request
from flask_cors import CORS
import json
import logging
from db import get_user_vector, user_login, set_user_vector, get_user_review
from utils import to_vector, predict_restaurant


logging.basicConfig(filename="app.log", level=logging.INFO)

app = Flask("app")
CORS(app)

user_id = -1
user_vector = ""


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


@app.route("/compute_user_vector")
def compute_user_vector():
    review = get_user_review(user_id)
    logging.warning("review: " + str(review))
    vector = to_vector(review)
    set_user_vector(user_id, vector)
    return {"message": "success", "content": "Compute vector success"}


@app.route("/predict")
def predict():
    global user_id
    user_vector_obj = get_user_vector(user_id)
    user_vector = user_vector_obj["user_vector"]
    logging.info("user_vector: " + str(user_vector))
    if user_vector != "default":
        result = predict_restaurant(user_vector)
        pass
    else:
        return {"message": "error", "content": "User vector does not exist!"}

    return {"message": "success", "content": "predict success", "result": result}


app.run(port=4000, debug=True)
