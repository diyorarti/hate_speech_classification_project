import os
import sys
import keras
import pickle
import numpy as np
import pandas as pd
from hate_speech.logger import logging
from hate_speech.exception import CustomException
from keras.utils import pad_sequences
from hate_speech.constant import *
from sklearn.metrics import confusion_matrix
from hate_speech.entity.config_entity import ModelEvaluationConfig
from hate_speech.entity.artifact_entity import ModelEvaluationArtifacts, ModelTrainerArtifacts, DataTransformationArtifacts

class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig,
                 model_trainer_artifacts: ModelTrainerArtifacts,
                 data_transformation_artifacts: DataTransformationArtifacts):
        """
        :param model_evaluation_config: Configuration for model evaluation
        :param model_trainer_artifacts: Output reference of model trainer artifact stage
        """

        self.model_evaluation_config = model_evaluation_config
        self.model_trainer_artifacts = model_trainer_artifacts
        self.data_transformation_artifacts = data_transformation_artifacts

    def evaluate(self, model, tokenizer, x_test, y_test):
        """
        :param model: Currently trained model or best model from local storage
        :param tokenizer: Tokenizer used for the model
        :param x_test: Test dataset features
        :param y_test: Test dataset labels
        :return: accuracy
        """
        try:
            logging.info("Entering into the evaluate function of Model Evaluation class")

            x_test = x_test['tweet'].astype(str)
            x_test = x_test.squeeze()
            y_test = y_test.squeeze()

            test_sequences = tokenizer.texts_to_sequences(x_test)
            test_sequences_matrix = pad_sequences(test_sequences, maxlen=MAX_LEN)
            logging.info(f"Test sequences matrix shape: {test_sequences_matrix.shape}")

            accuracy = model.evaluate(test_sequences_matrix, y_test)
            logging.info(f"Model evaluation accuracy: {accuracy}")

            lstm_prediction = model.predict(test_sequences_matrix)
            res = [1 if prediction[0] >= 0.5 else 0 for prediction in lstm_prediction]
            logging.info(f"Confusion Matrix:\n{confusion_matrix(y_test, res)}")

            return accuracy
        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_model_evaluation(self) -> ModelEvaluationArtifacts:
        """
        Method Name :   initiate_model_evaluation
        Description :   This function is used to initiate all steps of the model evaluation

        Output      :   Returns model evaluation artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Initiate Model Evaluation")
        try:
            logging.info("Loading currently trained model")
            trained_model = keras.models.load_model(self.model_trainer_artifacts.trained_model_path)
            with open('tokenizer.pickle', 'rb') as handle:
                load_tokenizer = pickle.load(handle)

            logging.info("Evaluating the currently trained model")
            trained_model_accuracy = self.evaluate(trained_model, load_tokenizer,
                                                   pd.read_csv(self.model_trainer_artifacts.x_test_path, index_col=0),
                                                   pd.read_csv(self.model_trainer_artifacts.y_test_path, index_col=0))

            model_evaluation_artifacts = ModelEvaluationArtifacts(is_model_accepted=True)
            logging.info("Returning the ModelEvaluationArtifacts")
            return model_evaluation_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
