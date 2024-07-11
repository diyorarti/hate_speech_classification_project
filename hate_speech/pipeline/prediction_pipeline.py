import os
import sys
import keras
import pickle
from PIL import Image
from hate_speech.logger import logging
from hate_speech.constant import *
from hate_speech.exception import CustomException
from keras.utils import pad_sequences
from hate_speech.components.data_transformation import DataTransformation
from hate_speech.entity.config_entity import DataTransformationConfig
from hate_speech.entity.artifact_entity import DataIngestionArtifacts

class PredictionPipeline:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "PredictModel", MODEL_NAME)
        self.data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig, data_ingestion_artifacts=DataIngestionArtifacts)
    
    def predict(self, text):
        """Predict the class of the given text."""
        logging.info("Running the predict function")
        try:
            load_model = keras.models.load_model(self.model_path)
            with open('tokenizer.pickle', 'rb') as handle:
                load_tokenizer = pickle.load(handle)
            
            text = self.data_transformation.concat_data_cleaning(text)
            text = [text]
            logging.info(f"Cleaned text: {text}")

            seq = load_tokenizer.texts_to_sequences(text)
            padded = pad_sequences(seq, maxlen=300)
            logging.info(f"Tokenized and padded sequence: {seq}")

            pred = load_model.predict(padded)
            logging.info(f"Prediction: {pred}")

            if pred > 0.3:
                logging.info("Prediction result: hate and abusive")
                return "hate and abusive"
            else:
                logging.info("Prediction result: no hate")
                return "no hate"
        except Exception as e:
            raise CustomException(e, sys) from e
    
    def run_pipeline(self, text):
        """Run the entire prediction pipeline."""
        logging.info("Entered the run_pipeline method of PredictionPipeline class")
        try:
            predicted_text = self.predict(text)
            logging.info("Exited the run_pipeline method of PredictionPipeline class")
            return predicted_text
        except Exception as e:
            raise CustomException(e, sys) from e
