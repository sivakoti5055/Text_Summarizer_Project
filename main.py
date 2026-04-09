from text_summarize.pipeline.Stage_01_data_ingestion_pipeline import DataIngestionPipeline
from text_summarize.logging import logger
from text_summarize.pipeline.Stage_02_data_validation_pipeline import DataValidationPipeline

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

