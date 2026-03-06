from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.logging.logger import logging
import sys

if __name__ == '__main__':
    try:

        training_pipeline_config = TrainingPipelineConfig()

        # -----------------------------
        # Data Ingestion
        # -----------------------------
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )

        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)

        logging.info("Initiating data ingestion")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        logging.info("Data ingestion completed")

        print(data_ingestion_artifact)

        # -----------------------------
        # Data Validation
        # -----------------------------

        data_validation_config = DataValidationConfig(
            training_pipeline_config=training_pipeline_config
        )

        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config
        )

        logging.info("Initiating data validation")

        data_validation_artifact = data_validation.initiate_data_validation()

        print(data_validation_artifact)

        logging.info("Data validation completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)