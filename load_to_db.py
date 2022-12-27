import pymongo
from pymongo import MongoClient
import logging

cluster = MongoClient(
    "mongodb+srv://RyLai:ussvbHKLJuV2HuOl@cluster-rylai.q7s2wht.mongodb.net/?retryWrites=true&w=majority"
)

db = cluster["LocalGuide"]
User = db["User"]
Restaurant = db["Restaurant"]


for user_id in user_data:
    User.insert_one({"_id": user_id, "user_vector": "default", "user_review": "review"})

for restaurant_id in restaurant_data:

    Restaurant.insert_one({"_id": user_id, "restaurant_vector": "default", "restaurant_review": "review"})
