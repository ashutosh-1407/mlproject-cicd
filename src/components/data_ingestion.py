import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from dataclasses import dataclass 


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            logging.info("Reading the dataset as dataframe")
            df = pd.read_csv("notebook/data/stud.csv")

            logging.info("Creating the artifacts directory if it doesn't exist")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is complete")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    ingestion_obj = DataIngestion()
    train_data_path, test_data_path = ingestion_obj.initiate_data_ingestion()

    transformtion_obj = DataTransformation()
    train_array, test_array, _ = transformtion_obj.initiate_data_transformation(train_data_path, test_data_path)

    trainer_obj = ModelTrainer()
    best_model_score = trainer_obj.initiate_model_trainer(train_array, test_array)
    print("best score", best_model_score)
