import pandas as pd
data={
    "name":["rathul","sakib","neymar"],
    "age":[10,20,30],
    "city":["frankfurt","america","brazil"]
}
df=pd.DataFrame(data)
print(df)
df.to_csv("output.csv",index=False)
#df.to_excel("output.xlsx")
#df.to_json("output.json")

