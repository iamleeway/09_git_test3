from pprint import pprint
import pandas as pd

data = [
    {
        "id" : 1,
        "name" : "Sin movimiento",
        "points" : 1,
        "lower_limit" : 0,
        "deleted" : 0
    },
    {
        "id" : 2,
        "name" : "Más de 25 km/h",
        "points" : 3,
        "lower_limit" : 25,
        "deleted" : 0
    }
]

# 为转换成df，需要把id单独拿出来，只需要一行：
ret = [{s['id'] : {k : v for k, v in s.items() if k != 'id'}} for s in data]

pprint(ret)
df = pd.DataFrame.from_records(data)
df.set_index('id', inplace=True)
print(df.T)