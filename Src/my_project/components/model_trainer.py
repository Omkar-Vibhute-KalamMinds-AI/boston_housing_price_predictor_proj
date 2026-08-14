import sys
import pandas as pd
from Src.my_project.logger import logger
from Src.my_project.exception import ModelTrainingException

def train_model(x_train, y_train):
    try:
        logger.info("Training started")
    #    model.fit(x_train, y_train)
        logger.info("Training complete ✅")
    except Exception as e:
        raise ModelTrainingException(e, sys) 
    