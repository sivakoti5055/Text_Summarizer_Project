from text_summarize.constants import *
from text_summarize.entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelTrainingConfig
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
    
    def data_validation_object(self)->DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
                
        data_val_object = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILE = config.ALL_REQUIRED_FILES
        )
        return data_val_object
    

    
    def get_data_transformation_object(self)->DataTransformationConfig:
        config = self.config.data_transformation
        data_object = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )
        return data_object
    
    def get_model_training_object(self)->ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.TrainingArguments
        model_trainer_config = ModelTrainingConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_ckpt = config.model_ckpt,
                num_train_epochs = params.num_train_epochs,
                warmup_steps = params.warmup_steps,
                per_device_train_batch_size = params.per_device_train_batch_size,
                weight_decay = params.weight_decay,
                logging_steps = params.logging_steps,
                evaluation_strategy = params.evaluation_strategy,
                eval_steps = params.evaluation_strategy,
                save_steps = params.save_steps,
                gradient_accumulation_steps = params.gradient_accumulation_steps
            )
        return model_trainer_config
    
