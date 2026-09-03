import pandas as pd
df= pd.read_csv("../../housetraning.csv")

print(df.head())
print(df.tail())
print(df.info())
missing = df.isna().sum()
print(missing[missing > 0])
print(df.describe())
print(df.duplicated().sum())
print(df[["Alley","FireplaceQu","GarageType"]])
print(df.iloc[4:10, 5:10 ])






# #missing value zero chara ber korbe
# missing = df.isna().sum()
# print(missing[missing > 0])
# #print(df.to_string())

