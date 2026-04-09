from text_summarize.components.data_ingestion import DataIngestion
from text_summarize.config.configuration import ConfigurationManager


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_object = config.data_ingestion_object()
        data_ingestion = DataIngestion(data_ingestion_object)
        data_ingestion.download_url()
        data_ingestion.exact_zip_file()