# list
import pandas as pd
data = [100, 102, 103]
series = pd.Series(data, index=["a", "b", "c"]   )
print(series)
series. loc["c"]=200
print(series)


#dictionary
data={"day 1": 1700, "day 2": 1800, "day 3": 1900}
series = pd.Series(data)
print(series)
series.loc["day 3"]+= 2000
print(series)