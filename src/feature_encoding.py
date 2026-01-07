import os
import pandas as pd
import logging
from abc import ABC, abstractmethod
from sklearn.preprocessing import OneHotEncoder
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Feature_Encoding_Strategy(ABC):
    @abstractmethod
    def encorder(self,df,columns):
        pass

# class Nominal_Encoding_Strategy(Feature_Encoding_Strategy):
#     def __init__(self,encoder_class):
#         self.encoder_class=encoder_class

#     def encorder(self,df,columns):
#         df_encord=df[columns]   
#         encorder=self.encoder_class(drop="first",sparse_output=False)
#         encoded_df=encorder.fit_transform(df_encord[columns])
#         encoded_df=pd.DataFrame(encoded_df,columns=encorder.get_feature_names_out(columns))    
#         df=pd.concat([df,encoded_df],axis=1)
#         df.drop(columns=columns,inplace=True)
#         return df
        
class Nominal_Encoding_Strategy(Feature_Encoding_Strategy):

    def encorder(self,df,columns):
        df_encord=df[columns]   
        encorder=OneHotEncoder(drop="first",sparse_output=False)
        encoded_df=encorder.fit_transform(df_encord[columns])
        encoded_df=pd.DataFrame(encoded_df,columns=encorder.get_feature_names_out(columns))    
        df=pd.concat([df,encoded_df],axis=1)
        df.drop(columns=columns,inplace=True)
        return df
            