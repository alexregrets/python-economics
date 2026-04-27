import pandas as pd
# Create a sample DataFrame


import pandas as pd

data = {
    'company': ['КАМАЗ', 'Газпром', 'Сбер', 'КАМАЗ', 'Газпром'],
    'year': [2021, 2021, 2021, 2022, 2022],
    'revenue': [250, 1200, 890, 310, 980]
}

df = pd.DataFrame(data)


print(df.groupby("company")["revenue"].mean())

#print(df.describe())

#print(df.groupby('company')['revenue'].agg(['mean','sum']))

# Define a function to categorize revenue
def revenue_category(r):
    if r > 500:
        return 'high'
    elif r >200:
        return 'medium'
    else:
        return 'low'
    
#df['r_category'] = df['revenue'].apply(revenue_category)
#print(df)




df['r_revenue'] = df['revenue'].apply(lambda r: 'high' if r > 500 else ('medium' if r > 200 else 'low'))
print(df)