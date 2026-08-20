import pandas as pd
df= pd.read_csv("../../titanictrain.csv",
             #   index_col="Name"
                )
print(
# df.shape,df.dtypes,df.info(),df.describe(),
df.columns
 )
#print(df.isna().any(axis=1).to_string()) ##shob column wise mising- 1ta missing holei true dibe for any()
#print(df.duplicated().to_string())
#print(df[df["Age"].isna()].to_string()) ##for one coloum
#print(df.isna().sum()) ##missing gular sum ber korbe i will know imediately k missing for cleaning atai useful
print(df.groupby(["Sex","Pclass"])["Age"].median())

###if sex-female and class type 1st,2nd,3rd the age
df["Age"]= df["Age"].fillna(df.groupby(["Sex","Pclass"])["Age"].transform("median"))
print(df[["Sex","Pclass","Age"]].to_string())

###
