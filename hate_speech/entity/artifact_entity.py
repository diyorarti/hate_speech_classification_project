from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    hatespeechdataset_data_file_path: str
    labeled_data_file_path: str
