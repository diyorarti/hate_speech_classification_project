# Hate Speech Classification
## Project Overview
This project aims to classify hate speech from a dataset containing tweets or text messages. It applies natural language processing (NLP) techniques, followed by training a deep learning model for classification.

## Folder Structure
```bash
hate_speech/
├── components/
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── model_evaluation.py
│   ├── model_trainer.py
├── constant/
│   ├── __init__.py
├── entity/
│   ├── __init__.py
│   ├── artifact_entity.py
│   ├── config_entity.py
├── exception/
│   ├── __init__.py
├── logger/
│   ├── __init__.py
├── ml/
│   ├── __init__.py
│   ├── models.py
├── pipeline/
│   ├── __init__.py
│   ├── prediction_pipeline.py
│   ├── train_pipeline.py
├── utils/
│   ├── __init__.py
│   ├── main_utils.py
├── notebooks/
│   ├── hate_speech_classification.ipynb
├── app.py
├── README.md
├── LICENSE
├── .gitignore
```
## Technologies Used

- Python: Core programming language.
- TensorFlow/Keras: For training the deep learning model.
- FastAPI: To serve the model as an API.
- DVC (Data Version Control): For versioning data and managing pipelines.
- gdown: To download datasets from Google Drive.
- Docker: To containerize the application.
- Jupyter Notebooks: For experiments and research.


# Key Components
**Data Ingestion**
Purpose: Downloads the dataset from Google Drive and extracts the necessary files.
Files:

- data_ingestion.py: Handles downloading and extracting files.
- dvc.yaml: Contains the data pipeline configuration.
Output: Data is stored in the artifacts/data_ingestion/ folder.
**Data Transformation**
Purpose: Cleans and transforms the dataset for training.
Files:
- data_transformation.py: Cleans and balances the data. Output: Transformed data is saved in artifacts/- - data_transformation/.
**Model Training**
Purpose: Trains an LSTM model on the hate speech dataset.
Files:
- model_trainer.py: Handles training and saving the model. Output: The trained model is saved as model.h5 in artifacts/trained_model/.
**Model Evaluation**
Purpose: Evaluates the trained model using test data.
Files:
- model_evaluation.py: Loads the model and computes evaluation metrics. Output: Evaluation results are stored in artifacts/model_evaluation/.
**Prediction Pipeline**
Purpose: Processes input text and returns a prediction for hate speech classification.
Files:
- prediction_pipeline.py: Loads the trained model and makes predictions.
**API Deployment**
Purpose: Deploys the trained model as an API for predictions.
Files:
- app.py: Contains FastAPI routes for training and prediction.
**Notebooks**
Contains Jupyter notebooks for experimentation:
- hate_speech_classification.ipynb

# Installation
## Prerequisites
- Python 3.8+
- TensorFlow/Keras
- FastAPI and Uvicorn
- DVC (Data Version Control)
- Docker (if using Docker for deployment)

**Setup**
Clone the repository:
```bash
git clone https://github.com/diyorarti/Hate-Speech-Classification.git
cd Hate-Speech-Classification
```
**Install dependencies:**
```bash
pip install -r requirements.txt
```
