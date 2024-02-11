import os
import sys
sys.path.insert(0, '.')
from src.exception import customExeption
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_con=DataIngestionConfig()

    def initiate_ingestion(self):
        logging.info("jsdhfjdshjfhjsdhjf")

        try:
            df = pd.csv_read('notebook\data\stud.csv')
            logging.info('data read')
            os.makedirs(os.path.dirname(self.data_ingestion_con.train_data_path), exist_ok = True)
            df.to_csv(self.data_ingestion_con.raw_data_path, index=False, Header=True)
            logging.info('test train initiated')
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)

            train_set.to_csv(self.data_ingestion_con.train_data_path, index=False, Header=True)
            test_set.to_csv(self.data_ingestion_con.test_data_path, index=False, Header=True)

            logging.info('doneeeeeeeeee')

            return (
                self.data_ingestion_con.train_data_path,
                self.data_ingestion_con.test_data_path

            )
        except Exception as e:
            customExeption(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_ingestion()