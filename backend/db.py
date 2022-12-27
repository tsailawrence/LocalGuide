import pymongo
from pymongo import MongoClient
import logging

cluster = MongoClient(
    "mongodb+srv://RyLai:ussvbHKLJuV2HuOl@cluster-rylai.q7s2wht.mongodb.net/?retryWrites=true&w=majority"
)

db = cluster["LocalGuide"]
User = db["User"]


def get_user_embedding(user_id):
    embedding = User.find_one({"_id": user_id}, {"_id": 0, "user_embedding": 1})
    return embedding


def get_user_review(user_id):
    review = User.find_one({"_id": user_id}, {"_id": 0, "user_review": 1})
    return review


def user_login(user_id):
    user = User.find_one({"_id": user_id}, {"_id": 1})
    if not user:
        User.insert_one({"_id": user_id, "user_embedding": "default", "user_review": "review"})  # review to be modified
    return "login success"


def set_user_embedding(user_id, new_embedding):
    logging.warning("id: " + str(user_id))
    logging.warning("embedding: " + str(new_embedding))
    User.find_one_and_update({"_id": user_id}, {"$set": {"user_embedding": new_embedding}})


# User.insert_one({"_id": 0, "user_embedding": "default"})

# User.find_one_and_update({"_id": 0}, {"$set": {"user_embedding": "something new"}})
