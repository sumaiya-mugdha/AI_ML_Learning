import pandas as pd
##csv file import
df= pd.read_csv("titanictrain.csv")

print(df.to_string()) ####all file load

#json file import
df = pd.read_json("titanic.json")
print(df.to_string())

##selection
# selection by coloum
print(df["Name"].to_string())
print(df[["Age","Fare","Sex"]])

# selection by row
print(df.loc[1])
df= pd.read_csv("titanictrain.csv", index_col="Age")
print(df.loc[30, ["PassengerId","Survived"]])

##int based slicing
print(df.iloc[30:40:3, 2:7])

#df= pd.read_csv("titanictrain.csv", index_col="Name")

###search

died=input("enter to know info: ")
try:
    print(df.loc[died])
except KeyError:
    print("f{died} do not exist")
