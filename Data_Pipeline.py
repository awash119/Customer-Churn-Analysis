from main import DataIngestorCSV
from config import get_data_path
from Handling_Missing_Value import ColumnRemover


def Data_Pipeline():
    file_path = get_data_path()
    ingestor = DataIngestorCSV()
    df = ingestor.ingest(file_path)
    print(f"Data Loaded Successfully {df.shape}")
    print(f"Columns: {df.columns.tolist()}")

    colremover= ColumnRemover()
    selected_columns=['RowNumber', 'CustomerId']
    colremover.columnsremove(df,selected_columns)
    print(f"Columns after removal: {df.columns.tolist()}")

Data_Pipeline()