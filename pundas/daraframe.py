from os import name

import pandas as pd

data = {"Name": ["i", "am", "cutie"],
        "Age": [20, 30, 40], }
df = pd.DataFrame(data , index= ["mugdha", "tasik", "shawana"])
#add new coloum
df["Job"]= ["Cook", "clean", "sleep"]
print(df)

# add a new row
new_row= pd.DataFrame([{"Name": "sandy", "Age": 28, "job": "lallu"}],
                      index= ["employee 4"])
df= pd.concat([df, new_row])
print(df)