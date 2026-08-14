from Src.my_project.exception import PredictionException
import sys
import pandas as pd
from Src.my_project.logger import logger


def predict(features):
    try:
        logger.info("Running prediction")
    #    result = model.predict(features)
    #    return result
    except Exception as e: 
        logger.error(f"Prediction failed: {e}")
        return {"error": "Prediction failed"} 