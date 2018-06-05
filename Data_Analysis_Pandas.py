import pandas as pd

excel_path="mosam.xlsx"

df= pd.read_excel(excel_path)
df.head()
print (df)

print("-----  Access certain columns ------ \n \n ")


y=df[['Number','College']]

print (y)


print("-----  Access certain cell using 'ÍX ' method------ \n \n ")

z=df.ix[1,1]
print (z)
