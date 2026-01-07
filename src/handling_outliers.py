import os
import pandas as pd
import logging
from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class OutlierDetectionStrategy(ABC):
    @abstractmethod
    def detect_outlier(self,df:pd.DataFrame,columns:list):
        pass

class IQROutlierDetection(OutlierDetectionStrategy):
    def detect_outlier(self,df,columns):
        outliers=pd.DataFrame(False,index=df.index,columns=columns)
        for col in columns:
            Q1=df[col].quantile(0.25)
            Q3=df[col].quantile(0.75)
            IQR=Q3-Q1
            outliers[col]= (df[col]<(Q1-1.5*IQR)) | (df[col]>(Q3+1.5*IQR))
        return outliers

class Outlier_Detector():
    def __init__(self,strategy):
        self.strategy=strategy

    def detect_outlier(self,df,columns):
        return self.strategy.detect_outlier(df,columns)  
    
    def handle_outliers(self,df,columns):
        outliers=self.strategy.detect_outlier(df,columns)  
        outliers_count=outliers.sum(axis=1)
        rows_to_remove=outliers_count>=2
        return df[~rows_to_remove]



