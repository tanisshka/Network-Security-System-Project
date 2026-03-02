from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion=DataIngestion(data_ingestion_config=dataIngestionConfig)
        logging.info("Initiate the data ingestion")
        dataingestionArtifacet=data_ingestion.initiate_data_ingestion()
        print(dataingestionArtifacet)
    except Exception as e:
        raise NetworkSecurityException(e,sys)