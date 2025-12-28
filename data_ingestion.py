import os
import pandas as pd
import logging

class DataIngestorCSV():
    def ingest(self, file_path, required_columns=None):
        try:
            df = pd.read_csv(file_path)
        except Exception:
            logging.exception("Failed to read CSV")
            raise
        return df
