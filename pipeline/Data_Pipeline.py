import os
import sys
import logging
from sklearn.preprocessing import OneHotEncoder
# ensure project root is on sys.path so sibling packages (src, utils) can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_ingestion import DataIngestorCSV
from src.handling_outliers import Outlier_Detector,IQROutlierDetection
from src.feature_binning import CustomBinningStrategy
from src.feature_encoding import Nominal_Encoding_Strategy
from utils.config import get_data_path,get_columns,feature_binning,feature_encoding



def Data_Pipeline():
    print("Step 01: Data Ingestion \n")
    file_path = get_data_path()
    ingestor = DataIngestorCSV()
    df = ingestor.ingest(file_path['raw_data_path'])
    logging.info(f"Data Loaded Successfully {df.shape}")
    logging.info(f"Columns: {df.columns.tolist()}")

    print(" \nStep 02:Handling Outliers")
    columns=get_columns()
    outlier_cols=columns['outlier_columns']
    out=Outlier_Detector(strategy=IQROutlierDetection())
    out.handle_outliers(df,outlier_cols)
    print(f"After Removing Outliers Data Shape {df.shape}")
    print(df.head())
    
    print("\nStep 03:Feature Binning")
    feature_bins=feature_binning()
    binnings=CustomBinningStrategy(feature_bins["credit_score_bins"])
    df=binnings.bin_feature(df,"CreditScore")
    print("Feature Binnign Completed")
    print(df.head())

    print("\nStep 04 Feature Encoding ")
    feature_encorder=feature_encoding()
    nominal_encoder=Nominal_Encoding_Strategy()
    df=nominal_encoder.encorder(df,feature_encorder["nominal_columns"])
    print(df.head())
    



Data_Pipeline()