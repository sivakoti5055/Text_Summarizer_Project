from text_summarize.components.model_training import ModelTraining
from text_summarize.config.configuration import ConfigurationManager

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(Self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_training_object()
            model_trainer_config = ModelTraining(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e
