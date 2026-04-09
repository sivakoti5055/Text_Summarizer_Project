from text_summarize.components.data_validation import DataValidation
from text_summarize.config.configuration import ConfigurationManager


class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_obj = config.data_validation_object()
            data_val = DataValidation(data_validation_obj)
            data_val.validation_status_check()
        except Exception as e:
            raise e
