import numpy as np


class Handling_Outliers:
    def outlier_identifier(self, df, col):
        numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']
        df_cp=df.copy()
        for col in numerical_cols:
            Q1=df_cp[col].quantile(0.25)
            Q3=df_cp[col].quantile(0.75)
            IQR=Q3-Q1
            lower_bound=Q1-1.5*IQR
            upper_bound=Q3+1.5*IQR
            df_cp[f'{col}_outliers']=((df_cp[col]<lower_bound)|(df_cp[col]>upper_bound))
            print(f'Number of outliers in {col}: {df_cp[f"{col}_outliers"].sum()}')
        df_cp[["CreditScore_outliers","Age_outliers","Tenure_outliers","Balance_outliers","EstimatedSalary_outliers"]] = df_cp[["CreditScore_outliers","Age_outliers","Tenure_outliers","Balance_outliers","EstimatedSalary_outliers"]].astype(np.int64)
        df_cp["Outlier_Count"] = df_cp[["CreditScore_outliers","Age_outliers","Tenure_outliers","Balance_outliers","EstimatedSalary_outliers"]].sum(axis=1)
        df_cp=df_cp[df_cp["Outlier_Count"]<2]
        print(f"Data shape after removing outliers: {df_cp.shape}")
        df_cp.drop(["CreditScore_outliers","Age_outliers","Tenure_outliers","Balance_outliers","EstimatedSalary_outliers","Outlier_Count"],axis=1,inplace=True)
        df=df_cp
        print(f"Data shape after removing outliers: {df_cp.shape}")
        return df