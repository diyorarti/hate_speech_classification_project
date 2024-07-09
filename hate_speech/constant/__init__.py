import os

from datetime import datetime


# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
FOLDER_NAME = 'Data'
GD_ZIP_FILE_PATH = "https://drive.google.com/uc?id=1_XsweOGUzjYDbQqibSvI8M3X1hvycd8F"
ZIP_FILE_NAME = 'hate_speech_datasets.zip'
LABEL = 'label'
TWEET = 'tweet'
MODEL_NAME = 'model.h5'
APP_HOST = "0.0.0.0"
APP_PORT = 8080

# data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_BALANCED_DATA_DIR = "HateSpeechDatasetBalanced.csv"
DATA_INGESTION_RAW_DATA_DIR = "labeled_data.csv"