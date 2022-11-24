import shutil
import yaml
from typing import List
import os,sys
from finance_complaint.logger import logger
from finance_complaint.exception import FinanceException

def write_yaml_file(file_path: str, data:dict = None):
    """
    create yaml file
    file_path: str
    data: dict
    """
    try:
        os.makedir(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, "w") as yaml_file:
            if data is not None:
                yaml.dump(data, yaml_file)
    except Exception as e:
        raise FinanceException(e, sys)

def read_yaml_file(file_path: str)-> dict:
    try:
        """
        Read YAML file and returns contents as dictionary
        file_path : str
        """
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise FinanceException(e, sys)
