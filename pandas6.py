import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats


df = pd.DataFrame({
    "region": ["МСК", "СПБ", "ЕКБ", "НСК"],
    "revenue": [1000, 800, 600, 400]
})



print(df.iloc[2:3])

print(df.loc[df["revenue"] > 500])


print(df.iloc[:, 0])
