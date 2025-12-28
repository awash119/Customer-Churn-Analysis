from data_ingestion import DataIngestorCSV
from config import get_data_path
from Handling_Missing_Value import ColumnRemover
from Handling_Outliers import Handling_Outliers


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

    outlier_handler=Handling_Outliers()
    numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']
    df=outlier_handler.outlier_identifier(df,numerical_cols)
    

Data_Pipeline()