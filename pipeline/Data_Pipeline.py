import os
import sys
import logging
# ensure project root is on sys.path so sibling packages (src, utils) can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_ingestion import DataIngestorCSV
from utils.config import get_data_path



def Data_Pipeline():
    print("Step 01: Data Ingestion \n")
    file_path = get_data_path()
    ingestor = DataIngestorCSV()
    df = ingestor.ingest(file_path['raw_data_path'])
    logging.info(f"Data Loaded Successfully {df.shape}")
    logging.info(f"Columns: {df.columns.tolist()}\n")

    print("Step 02:Handling Outliers \n")


Data_Pipeline()