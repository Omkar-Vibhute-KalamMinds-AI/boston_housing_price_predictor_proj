from Src.my_project.logger import logging
from Src.my_project.exception import CustomException
from Src.my_project.components.data_ingestion import DataIngestion
from Src.my_project.components.data_ingestion import DataIngestionConfig
import sys
import dotenv

if __name__ == '__main__':  
    logging.info('The operation has started')
    
    try:
        data_ingestion_config = DataIngestionConfig() 
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.init_data_ingestion() 
        
        logging.info(f'Train path: {train_path}')
        logging.info(f'Test path: {test_path}')

    except Exception as e:
        logging.error('Pipeline failed')
        raise CustomException(e, sys)  
    
    