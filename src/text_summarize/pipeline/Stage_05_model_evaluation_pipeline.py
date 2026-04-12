from text_summarize.components.model_evaluation import ModelEvaluation
from text_summarize.config.configuration import ConfigurationManager


class ModelEvalutaionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()