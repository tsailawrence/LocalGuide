from transformers import (
    AutoModelForMaskedLM,
    AutoConfig,
    AutoTokenizer
)
import torch
import torch.nn as nn

import copy

class BertRecommender(nn.Module):
    def __init__(self, model_path=None):
        super(BertRecommender, self).__init__()
        self.config = AutoConfig.from_pretrained('hfl/chinese-macbert-large')

        self.bert_model = AutoModelForMaskedLM.from_pretrained(
            'hfl/chinese-macbert-large',
            from_tf=bool(".pkg" in model_path),
            config=self.config,
        )
        self.bert_model.bert.encoder.layer = self.bert_model.bert.encoder.layer[:1]
        self.bert_rest_model = copy.deepcopy(self.bert_model)
        self.mapping = nn.Sequential(
            nn.Linear(1024, 1),
        )
        self.sigmoid = nn.Sigmoid()
        self.layerNorm = nn.LayerNorm([512])
        
    def forward(self, x):
        (user_outputs, rest_outputs, label_outputs) = x
        # print(user_outputs)
        batch_size = label_outputs.size(0)
        user = self.mapping(
            self.bert_model.forward(**user_outputs, return_dict=True, output_hidden_states=True)['hidden_states'][-1]
        ).view(batch_size, -1)

        rest = self.mapping(
            self.bert_rest_model.forward(**rest_outputs, return_dict=True, output_hidden_states=True)['hidden_states'][-1]
        ).view(batch_size, -1)
        
        return torch.mul(user, rest).sum(dim=1)
    
    def getUserRepresentation(self, x):
            user_outputs = x
            user = self.mapping(
                self.bert_model.forward(**user_outputs, return_dict=True, output_hidden_states=True)['hidden_states'][-1]
            )
            return user

    def getRestaurantRepresentation(self, x):
            rest_outputs = x
            rest = self.mapping(
                self.bert_model.forward(**rest_outputs, return_dict=True, output_hidden_states=True)['hidden_states'][-1]
            )
            return rest
        
    def evalModel(self, user, rest):
        return torch.mul(user, rest).sum(dim=1)


class BertRecommen_Tokenizer():
    def __init__(self, model_path):
        self.Tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
    def __call__(self, input): 
        return  self.Tokenizer(
            input,
            truncation=True,
            padding='max_length',
            max_length= 512, #args.max_length,
            return_tensors='pt'
        )
        
        
    
