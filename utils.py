import datetime


def to_vector(review: str) -> str:
    return "new_vector at: " + str(datetime.datetime.now())


def predict_restaurant(user_vector: str) -> list:
    return "prediction"
