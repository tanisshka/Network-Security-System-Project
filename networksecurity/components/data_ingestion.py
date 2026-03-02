import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataingestionArtifact
from dotenv import load_dotenv
load_dotenv()

password=os.getenv("DB_PASSWORD")
username=os.getenv("DB_USERNAME")

MONGO_DB_URL = f"mongodb+srv://{username}:{password}@cluster0.do179sg.mongodb.net/?appName=Cluster0"

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):
        """
        Read data from mongodb
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongoClient = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongoClient[database_name][collection_name]

            records = list(collection.find())

            df = pd.DataFrame(records)

            if df.shape[0] == 0:
                raise Exception("No data found in MongoDB")

            if "_id" in df.columns:
                df.drop("_id", axis=1, inplace=True)

            df.replace({"na": np.nan}, inplace=True)
            print("Shape:", df.shape)

            return df
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        """
        Exporting raw data
        """
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_name=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_name,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
             
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        """
        Export train and test data
        """
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ration)
            logging.info("Performed train test split on the dataframe")
            
            dir_name=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_name,exist_ok=True)
            
            logging.info("Exporting train and test file path")
            
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            
            logging.info("Exported train and test data")
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact=DataingestionArtifact(self.data_ingestion_config.training_file_path,self.data_ingestion_config.testing_file_path)
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
"""
My pipeline reads data from MongoDB, converts it into a DataFrame, 
stores a raw copy in a feature store, performs train-test split, saves train and test datasets, 
and returns artifact paths for downstream components. The entire process is version-controlled 
using timestamp-based artifact directories
"""