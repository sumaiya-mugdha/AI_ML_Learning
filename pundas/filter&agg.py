   #filtering

import pandas as pd
df= pd.read_csv("titanictrain.csv")
dead= df[df["Survived"]== False]
print(dead["Name"])