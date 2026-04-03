from text_summarize.pipeline.Stahe_01_data_ingestion_pipeline import DataIngestionPipeline
from text_summarize.logging import logger

STAGED_NAME = "Data Ingestion Stage"
try:
    logger.info("stage {STAGED_NAME} is started")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info("stage {STAGED_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e

