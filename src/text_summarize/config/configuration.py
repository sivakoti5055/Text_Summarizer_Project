from text_summarize.constants import *
from text_summarize.entity import DataIngestionConfig
from text_summarize.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

    def data_ingestion_object(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_object =  DataIngestionConfig(
            root_dir = config.root_dir,
            source_url= config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_object