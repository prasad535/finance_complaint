from finance_complaint.exception import FinanceException
from finance_complaint.logger import logger

from finance_complaint.config.pipeline_config import FinanceConfig
from finance_complaint.entity.artifact_entity import DataIngestionArtifact

import sys

class TrainingPipeline:
    def __init__(self, finance_config: FinanceConfig):
        self.finance_config: FinanceConfig = finance_config

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion_config = self.finance_config.get_data_ingestion_config()
            
        except Exception as e:
            raise FinanceException(e, sys)