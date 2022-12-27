import pymongo
from pymongo import MongoClient
import logging

cluster = MongoClient(
    "mongodb+srv://RyLai:ussvbHKLJuV2HuOl@cluster-rylai.q7s2wht.mongodb.net/?retryWrites=true&w=majority"
)

db = cluster["LocalGuide"]
User = db["User"]


def get_user_vector(user_id):
    vector = User.find_one({"_id": user_id}, {"_id": 0, "user_vector": 1})
    return vector


def get_user_review(user_id):
    review = User.find_one({"_id": user_id}, {"_id": 0, "user_review": 1})
    return review


def user_login(user_id):
    user = User.find_one({"_id": user_id}, {"_id": 1})
    if not user:
        User.insert_one({"_id": user_id, "user_vector": "default", "user_review": "review"})  # review to be modified
    return "login success"


def set_user_vector(user_id, new_vector):
    logging.warning("id: " + str(user_id))
    logging.warning("vector: " + str(new_vector))
    User.find_one_and_update({"_id": user_id}, {"$set": {"user_vector": new_vector}})


# User.insert_one({"_id": 0, "user_vector": "default"})

# User.find_one_and_update({"_id": 0}, {"$set": {"user_vector": "something new"}})
