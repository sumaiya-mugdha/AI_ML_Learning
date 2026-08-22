import pandas as pd
df= pd.read_csv("../../titanictrain.csv")
# # df.shape,df.dtypes,df.info(),df.describe(),
# df.columns
#  )
#print(df.isna().any(axis=1).to_string()) ##shob column wise mising- 1ta missing holei true dibe for any()
#print(df.duplicated().to_string())
#print(df[df["Age"].isna()].to_string()) ##for one coloum
#print(df.isna().sum()) ##missing gular sum ber korbe  will know imediately k missing for cleaning atai useful
#print(df.groupby(["Sex","Pclass"])["Age"].median())
#print(df.groupby("Embarked")["Embarked"].count().to_string())


# ###if sex-female and class type 1st,2nd,3rd the age
df["Age"]= df["Age"].fillna(df.groupby(["Sex","Pclass"])["Age"].transform("median"))
# # print(df[["Sex","Pclass","Age"]].to_string())
#
# ###for cabin we will extract the cabin name from the 1st string and the null will renamed as unknown
df["Deck"]= df["Cabin"].str[0].fillna("Unknown")
# print(df[["Name","Deck","Survived"]].to_string())
# # print(df.groupby(["Deck","Survived"])["Name"].count().to_string()) ####interesting

##for embareked- use median
df["Embarked"]= df["Embarked"].fillna(df["Embarked"].mode()[0])
#print(df["Embarked"].to_string())

###no incorrect data till now

###finding more for feature engg.
# age= df[((df["Age"]<5) | (df["Age"]> 100)) & (df["Survived"] == 0)]
# print(age[["Name", "SibSp", "Parch","Survived"]])
# family=df.groupby(["Ticket","Pclass","SibSp","Parch","Cabin"])["Name"].count()
#
# show= family[family> 1]
# print(show.to_string())

##Family size
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
##IS ALONE OR NOT
df["IsAlone"] = (df["SibSp"]==0) & (df["Parch"]==0)
#AgeGroup
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 17, 59, 100],
    labels=["Child", "Teen", "Adult", "Senior"]
)
##rename a column and drop one
df= df.drop(columns=["Cabin"])

##agg()- want to define multiple statistic
print(df[["Age", "Fare"]].agg(["mean", "median", "min", "max"]))
print("Missing values:")
print(df.isna().sum())

print("\nData types:")
print(df.dtypes)

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())