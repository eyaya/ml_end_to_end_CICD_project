import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngenstionConfig:
    train_data_path = os.path.join('artifact', 'train.csv')
    test_data_path = os.path.join('artifact', 'test.csv')
    raw_data_path = os.path.join('artifact', 'raw.csv')
    
    
class DataIngenstion:
    def __init__(self):
        self.ingenstion_config = DataIngenstionConfig()
        
    def initiate_data_ingenstion(self):
        logging.info("Entered the data ingenstion method or compnent")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingenstion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingenstion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state = 42 )
            train_set.to_csv(self.ingenstion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingenstion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")
            return(
                self.ingenstion_config.train_data_path,
                self.ingenstion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    obj = DataIngenstion()
    obj.initiate_data_ingenstion()
    