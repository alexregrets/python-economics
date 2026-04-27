import pandas as pd 


df1 = pd.DataFrame({
    'company': ['КАМАЗ', 'Газпром', 'Сбер'],
    'revenue': [280, 1090, 890]
})

df2 = pd.DataFrame({
    'company': ['КАМАЗ', 'Газпром', 'ВТБ'],
    'employees': [50000, 480000, 75000]
})


#print(df1)
#print(df2)


print(pd.merge(df1,df2, on = 'company', how = 'inner'))

