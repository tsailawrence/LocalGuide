import torch
from functools import cache
from model import BertRecommender
from model import BertRecommen_Tokenizer

class microservice_for_rec:
    def __init__(self, ckpt_path):     
        self.model = BertRecommender(ckpt_path)
        print('hi!')
        self.model.load_state_dict(torch.load(ckpt_path))
        self.tokenizer = BertRecommen_Tokenizer('hfl/chinese-macbert-large')

    @cache
    def GetUserRepresentation(self, reviews):
        
        reviews_tokenized = self.tokenizer(reviews)
        user_representation = self.model.getUserRepresentation(reviews_tokenized)
        return user_representation
    
    @cache
    def GetRestaurantRepresentation(self, reviews):
        #print(reviews)
        reviews_tokenized = self.tokenizer(reviews)
        rest_representation = self.model.getRestaurantRepresentation(reviews_tokenized)
        return rest_representation
    
    def RecommendRestaurant(self, user_embedding, rest_embedding):
        rest_score = self.model.evalModel(user_embedding,rest_embedding)
        return rest_score
    
    
    
