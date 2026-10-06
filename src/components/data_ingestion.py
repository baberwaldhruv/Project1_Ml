import os
import sys
from src.exceptions import customexception
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class dataIngestionConfig:
    train_data_path:str = os.path.join('artifact','train.csv')
    test_data_path:str = os.path.join('artifact','test.csv')
    raw_data_path:str = os.path.join('artifact','data.csv')

class dataIngestion:
    def __init__(self):
        self.ingestionconfig = dataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("entered data ingestion")
        try:
            df = pd.read_csv('Notebook/StudentsPerformance.csv')
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)
            df.to_csv(self.ingestionconfig.raw_data_path,index=False,header=True)
            logging.info("train_train_split_initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestionconfig.train_data_path,index= False,header = True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index= False,header = True)
            logging.info("ingestion completed")
            return(
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path
            )
        except Exception as e:
            raise customexception(e,sys)

if __name__=="__main__":
    obj = dataIngestion()
    obj.initiate_data_ingestion()