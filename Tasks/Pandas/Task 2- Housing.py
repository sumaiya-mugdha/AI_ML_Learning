import pandas as pd
df= pd.read_csv("../../housetraning.csv")
#missing value zero chara ber korbe
missing = df.isna().sum()
print(missing[missing > 0])
#print(df.to_string())

