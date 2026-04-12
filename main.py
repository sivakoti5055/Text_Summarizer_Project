from text_summarize.pipeline.Stage_01_data_ingestion_pipeline import DataIngestionPipeline
from text_summarize.logging import logger
from text_summarize.pipeline.Stage_02_data_validation_pipeline import DataValidationPipeline
from text_summarize.pipeline.Stage_03_data_transformation_pipeline import DataTransformationPipeline
from text_summarize.pipeline.Stage_04_model_training_pipeline import ModelTrainingPipeline

STAGED_NAME = "Data Ingestion Stage"
try:
    logger.info("stage {STAGED_NAME} is started")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info("stage {STAGED_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGED_NAME = "Data Validation Stage"
try:
    logger.info("stage {STAGED_NAME} is started")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info("stage {STAGED_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGED_NAME = "Data Transformation Stage"
try:
    logger.info("stage {STAGED_NAME} is started")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info("stage {STAGED_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGED_NAME = "Model Training Stage"
try:
    logger.info("stage {STAGED_NAME} is started")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info("stage {STAGED_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e


