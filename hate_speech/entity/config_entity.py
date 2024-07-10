from dataclasses import dataclass
from hate_speech.constant import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.FOLDER_NAME: str = FOLDER_NAME
        self.ZIP_FILE_NAME: str = ZIP_FILE_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_BALANCED_DATA_DIR)
        self.NEW_DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_RAW_DATA_DIR)
        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)
        self.GD_ZIP_FILE_PATH = GD_ZIP_FILE_PATH

@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRANSFORMED_FILE_PATH = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_FILE_NAME)
        self.AXIS = AXIS
        self.INPLACE = INPLACE 
        self.DROP_COLUMNS = DROP_COLUMNS
        self.LABEL = LABEL
        self.LABEL1 = LABEL1
        self.CLASS = CLASS
        self.TWEET = TWEET