import pandas as pd

df = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104, 105, 106],
    "CreditScore": [450, 620, 710, 780, 820, 300]
})

def credit_category(score):
    if 300 <= score < 580:
        return "Poor"
    elif 580 <= score < 670:
        return "Fair"
    elif 670 <= score < 740:
        return "Good"
    elif 740 <= score < 800:
        return "Very Good"
    else:
        return "Excellent"

df["Category_apply"] = df["CreditScore"].apply(credit_category)
df["Category_map"] = df["CreditScore"].map(credit_category)

bins = [300, 580, 670, 740, 800, 850]
labels = ["Poor", "Fair", "Good", "Very Good", "Excellent"]

df["Category_cut"] = pd.cut(
    df["CreditScore"],
    bins=bins,
    labels=labels,
    right=False
)

print(df)
df.head()
