from pathlib import Path
import json

class Hyper_parameters():
    def __init__(self):
        ## MODEL
        self.model_name_or_path = 'hfl/chinese-macbert-large'
        ## PRECISION
        self.use_fp16 = True
        
        ## OPTIMIZER
        # self.learning_rate = 2e-4
        # self.weight_decay = 0.0
        # self.lr_scheduler_type = 'linear'
        
        ## TRAINING CONFIG
        # self.do_train = True
        self.test_file = self.handleTrainingFile()
        # self.scheduler_type = 'linear'
        self.seed = 99
        # self.per_device_train_batch_size = 4
        self.gradient_accumulation_steps = 1 #8
        self.max_length = 512
        
        # self.num_train_epochs = 1 #3
        
        # ## OTHERS
        # self.max_train_steps = None
        # self.num_warmup_steps = 0
        # self.with_tracking = False
        
        # ## OUTPUT DIR
        # self.output_dir = "./model"
        # self.checkpointing_steps = 'epoch'
        
    def handleTrainingFile(self):
        return (
            './restaurant_preference.json',
            './user_preference.json',
            './test.json',
        )