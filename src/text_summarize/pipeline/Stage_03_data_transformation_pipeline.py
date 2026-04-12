from text_summarize.components.data_transformation import DataTransformation
from text_summarize.config.configuration import ConfigurationManager

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_trans_obj = config.get_data_transformation_object()
            data_transformation = DataTransformation(data_trans_obj)
            data_transformation.convert()
        except Exception as e:
            raise e

            

    
