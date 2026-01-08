import os
import pandas as pd
import logging
from abc import ABC, abstractmethod
from sklearn.preprocessing import OneHotEncoder
import logging
from sklearn.preprocessing import StandardScaler


class Feature_Scaling_Strategy(ABC):
    def scale(self,df,columns):
        pass

class Standard_Scaler_Strategy():
    def __init__(self,strategy):
        self.strategy=strategy

    def scale(df,columns):
        scaler=StandardScaler()
        df_col_to_scale=df[columns]
        df=df.drop(columns=columns,axis=1)
        df_col_to_scale=scaler.fit_transform(df_col_to_scale[columns])
        df_col_to_scale=pd.DataFrame(df_col_to_scale,columns=columns,index=df.index)
        df=pd.concat([df,df_col_to_scale],axis=1)
        return df



