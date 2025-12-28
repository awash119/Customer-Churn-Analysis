import pandas as pd



class ColumnRemover():
    def columnsremove(self,df,selected_columns):
        df.drop(columns=selected_columns, axis=1, inplace=True)
        return df