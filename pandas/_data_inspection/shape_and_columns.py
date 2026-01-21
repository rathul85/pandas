

# -how big is your dataset_length
# -columns names()
import pandas as pd
data={
    "name":["ratul","saion","sakib","neymar","abd"],
    "age":[10,20,21,5,30],
    "city":["dhaka","german","america","brazil","sa"],
    "perfomance":[10,9,8,9,7]

}
df=pd.DataFrame(data)
print(df)
print(f'shape:{df.shape}')
print(f'columns:{df.columns}')
