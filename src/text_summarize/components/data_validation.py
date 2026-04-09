import os
from text_summarize.config.configuration import ConfigurationManager


class DataValidation:
    def __init__(self,config:ConfigurationManager):
        self.config = config

    def validation_status_check(self)->bool:
        validation_status = False
        try:
            all_files = os.listdir(
            os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            )
            validation_status = True
            for data in self.config.ALL_REQUIRED_FILE:
                if data not in all_files:
                    validation_status = False
                    break
        except:
             validation_status = False
              
        with open(self.config.STATUS_FILE,'w') as f:
            f.write(f"validation status:{validation_status}")

        return validation_status
          
            
