import os
import sys
import logging
from sklearn.preprocessing import OneHotEncoder,StandardScaler
# ensure project root is on sys.path so sibling packages (src, utils) can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_ingestion import DataIngestorCSV
from src.handling_outliers import Outlier_Detector,IQROutlierDetection
from src.feature_binning import CustomBinningStrategy
from src.feature_encoding import Nominal_Encoding_Strategy,Ordinal_Encoding_Strategy
from src.feature_scaling import Standard_Scaler_Strategy
from src.data_splitting import Train_Test_Split
from utils.config import get_data_path,get_columns,feature_binning,feature_encoding,feature_scaling



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

    print("\nStep 4.1 Nominal Feature Encoding ")
    feature_encorder=feature_encoding()
    nominal_encoder=Nominal_Encoding_Strategy()
    df=nominal_encoder.encorder(df,feature_encorder["nominal_columns"])
    print(df.head())

    print("\nStep 4.2 Ordinal Feature Encoding ")
    ordinal_encoder=Ordinal_Encoding_Strategy(feature_encorder["ordinal_mappings"]["CreditScoreBins"])
    df=ordinal_encoder.encorder(df,"CreditScoreBins")
    print(df.head())
    

    print("\nStep 5 Feature Scalling Strategy")
    feature_scaler=feature_scaling()
    Standard_Scaler=Standard_Scaler_Strategy(StandardScaler)
    df=Standard_Scaler_Strategy.scale(df,feature_scaler["columns_to_scale"])
    print(df.head())

    print("\nStep 6 Post Processing Started")
    print(file_path['data_artifacts_dir'])
    splitter=Train_Test_Split()
    Train_Test_Split.split(df=df,paths=file_path['data_artifacts_dir'])




Data_Pipeline()