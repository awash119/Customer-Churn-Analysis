import os
import pandas as pd
import logging
from abc import ABC, abstractmethod
from sklearn.preprocessing import OneHotEncoder
import logging
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class DataSplittingStrategy(ABC):
    def split(self,df,paths):
        pass

class Train_Test_Split(DataSplittingStrategy):
    
    def split(df,paths):
        os.makedirs(paths, exist_ok=True)
        X=df.drop(columns=["Exited"],axis=1)
        y=df["Exited"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train.to_csv(os.path.join(paths, "X_train.csv"), index=False)
        X_test.to_csv(os.path.join(paths, "X_test.csv"), index=False)
        y_train.to_csv(os.path.join(paths, "y_train.csv"), index=False)
        y_test.to_csv(os.path.join(paths, "y_test.csv"), index=False)
        print("Data Splitting Completed")


