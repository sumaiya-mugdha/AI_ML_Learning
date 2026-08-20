###filtering
#equal,less,greater-any number, string
import pandas as pd
df= pd.read_csv("titanictrain.csv")
dead= df[df["Survived"]== False]
print(dead["Name"])

####aggregate
#max,min,mean,count
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.mean(numeric_only=True))
print(df.count())

##single  column
print("the age is : ", df["Age"].count())
print("the mean is : ", df["Age"].mean())

##grounpby
group = df.groupby("Sex")
print(group["Survived"].count())

### HOW MANY MALE OR FEMALE SURVIVED FROM AGE 10 - 30
filter= df[(df["Age"].between(10,30)) & (df["Survived"]==1)]
group = filter.groupby("Sex")
print(group["Survived"].count())