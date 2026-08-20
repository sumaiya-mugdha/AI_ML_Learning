import pandas as pd
df= pd.read_csv("titanictrain.csv")

###missing values
##drop the coloum
df= df.drop(columns=["Cabin"])
print(df.to_string())

#drop the row-dropna- drop if not avaiable
df= df.dropna(subset=["Age"])
# print(df.to_string())
print(df.count())

#fill the row-fillna
fill=df.fillna({"Age":0})
print(df.count())

#FILL THE AGE WITH MEAN OF AGE
#indirect style
mean_age= df["Age"].mean()
fill=df.fillna({"Age":mean_age})
print(fill.to_string())
##direct style
df["Age"]= df["Age"].fillna(df["Age"].mean())
print(df.to_string())

###Fix inconsistent value
df["Cabin"]= df["Cabin"].replace({"C85":"no cabin"})
print(df.to_string())

###fix data type
df["Survived"]= df["Survived"].astype(bool)
print(df["Survived"])

###drop the duplicate
df= df["Age"].drop_duplicates()
print(df.to_string())
print(df.count())