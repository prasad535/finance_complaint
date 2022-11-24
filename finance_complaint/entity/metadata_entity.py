import os, sys
from finance_complaint.logger import logger
from finance_complaint.exception import FinanceException
from finance_complaint.utils import read_yaml_file, write_yaml_file
from collections import namedtuple
from dataclasses import dataclass

# class DataIngestionMetaDataInfo:
#     from_date: str
#     to_date: str
#     data_file_path: str

DataIngestionMetaDataInfo = namedtuple("DataIngestionMetaDataInfo", ["from_date", "to_date", "data_file_path"])

class DataIngestionMetaData:

    def __init__(self, metadata_file_path: str):
        self.metadata_file_path = metadata_file_path

    @property # it is as attribute to class
    def is_metadata_file_present(self):
        return os.path.exists(self.metadata_file_path)
    
    def write_meta_info(self, from_date: str, to_date: str, data_file_path: str):
        try:
            metadata_info = DataIngestionMetaDataInfo(
                from_date = from_date,
                to_date = to_date,
                data_file_path = data_file_path
            )
            write_yaml_file(file_path = self.data_file_path, data=metadata_info._asdict())

        except Exception as e:
            raise FinanceException(e, sys)

    def get_metadata_info(self)->DataIngestionMetaDataInfo:
        try:
            if not self.is_metadata_file_present:
                raise Exception("No metadata file available")

            metadata = read_yaml_file(self.metadata_file_path)
            metadata_info = DataIngestionMetaDataInfo(**(metadata))
            logger.info(metadata)
            return metadata_info
        except Exception as e:
            raise FinanceException(e,sys)
    

