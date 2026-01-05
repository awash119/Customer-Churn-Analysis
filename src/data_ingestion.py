import os
import pandas as pd
import logging
from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path):
        pass

class DataIngestorCSV(DataIngestor):
    def ingest(self, file_path:str) -> pd.DataFrame:
        try:
            df = pd.read_csv(file_path)
        except Exception:
            logging.exception("Failed to read CSV")
            raise
        return df
