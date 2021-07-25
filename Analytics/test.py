lst = ['any']*3
print(lst)

import pandas as pd

df1 = {
    'name':['echo','sky'],
    'age':[18,20]
}
df2 = df1.copy()
df3 = df1.copy()

df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)

writer = pd.ExcelWriter('testWriter.xlsx')
df1.to_excel(writer,startcol=2)
df2.to_excel(writer,startcol=6)
writer.save()