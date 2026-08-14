# It's for generic fuinctionality like reading the source data

import os
import sys
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus  
from Src.my_project.logger import logger, logging   
from Src.my_project.exception import CustomException 

load_dotenv(dotenv_path=r'D:\DataSciene Proj\.env')

host     = os.getenv('db_host')
username = os.getenv('db_username')
password = quote_plus(os.getenv('db_password')) 
port     = os.getenv('db_port')
db       = os.getenv('db_name')

print("HOST :", host)
print("USER :", username)
print("PORT :", port)
print("DB   :", db) 
print("PASS :", password) 


def read_sql_data():
    logging.info('Reading SQL database started')
    try:
        connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{db}"
        logging.info(f'Connecting to: {host}:{port}/{db}')

        engine = create_engine(connection_string)
        logging.info('SQLAlchemy engine created')

        df = pd.read_sql_query('SELECT * FROM bank_customers', engine)
        logging.info(f'Data loaded. Shape: {df.shape}')

        print(df.sample(5))
        return df

    except Exception as e:
        raise CustomException(e, sys) 
