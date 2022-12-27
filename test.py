from service import microservice_for_rec 
from predict_parameter import Hyper_parameters
from pathlib import Path
import json

args = Hyper_parameters()

mapper = {}

with open(Path(args.test_file[0]), 'r') as reader:
    mapper["restaurant"] = json.loads(reader.read())

with open(Path(args.test_file[1]), 'r') as reader:
    mapper["user"] = json.loads(reader.read())
    
with open(Path(args.test_file[2]), 'r') as reader:
    mapper["test"] = json.loads(reader.read())
    
    
    
service = microservice_for_rec('model.pkg')

# for i in range(len(mapper['test']))

for i in range(1,10):
    #user_embeddinbg = service.GetUserRepresentation( mapper["user"][mapper['test'][i]["user"]])
    user_embeddinbg = service.GetUserRepresentation('，，，，，。')
    rest_embeddinbg = service.GetRestaurantRepresentation(mapper["restaurant"][mapper['test'][i]["restaurant"]])
    #rest_embeddinbg = service.GetRestaurantRepresentation("我愛健康清淡")
    score = service.RecommendRestaurant(user_embeddinbg,rest_embeddinbg)
    print('score',score, mapper['test'][i]['rating'])