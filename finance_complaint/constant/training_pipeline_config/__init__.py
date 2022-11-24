import os

PIPELINE_NAME = "finance-comaplaint"
PIPELINE_ARTIFACT_DIR = os.path.join(os.getcwd(),"finance-artifact")

from finance_complaint.constant.training_pipeline_config.data_ingestion import *
from finance_complaint.constant.training_pipeline_config.data_validation import *
from finance_complaint.constant.training_pipeline_config.data_transformation import *
from finance_complaint.constant.training_pipeline_config.data_trainer import *
from finance_complaint.constant.training_pipeline_config.data_evaluation import *
from finance_complaint.constant.training_pipeline_config.data_pusher import *