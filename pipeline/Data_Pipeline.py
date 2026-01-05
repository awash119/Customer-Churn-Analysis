import os
import sys
import logging
# ensure project root is on sys.path so sibling packages (src, utils) can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_ingestion import DataIngestorCSV
from utils.config import get_data_path
from src.Handling_Missing_Value import ColumnRemover
from src.Handling_Outliers import Handling_Outliers


def Data_Pipeline():
    file_path = get_data_path()
    ingestor = DataIngestorCSV()
    df = ingestor.ingest(file_path)
    logging.info(f"Data Loaded Successfully {df.shape}\n")
    logging.info(f"Columns: {df.columns.tolist()}\n")

    colremover= ColumnRemover()
    selected_columns=['RowNumber', 'CustomerId']
    colremover.columnsremove(df,selected_columns)
    logging.info(f"Columns after removal: {df.columns.tolist()}\n")

    outlier_handler=Handling_Outliers()
    numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']
    df=outlier_handler.outlier_identifier(df,numerical_cols)
    logging.info(f"Data after outlier removal: {df.shape}\n")

if __name__ == "__main__":
    Data_Pipeline()