import pandas as pd 
import statsmodels.api as sm 
from scipy import stats

data = {
    "Y":  [91.0,90.5,91.5,88.8,90.4,93.3,93.6,94.1,93.6,95.0,
            96.0,96.3,95.9,96.7,97.1,97.6,98.0,97.9,97.8,98.9,
            99.0,98.4,98.9,99.3,99.3,99.4,99.4,99.9,100.1,100.2],
    "X1": [14.4,13.1,12.5,11.4,10.8,11.1,11.2,11.4,11.2,11.0,
            10.9,10.9,10.7,11.1,10.6,10.3,10.3,10.2,10.3,10.0,
            10.2,10.2,10.2,9.9,9.6,9.1,9.1,8.9,8.5,8.3]
}

df = pd.DataFrame(data)
print(df.head())
print(df.info())
X = sm.add_constant(df["X1"])
model = sm.OLS(df["Y"], X).fit()
print(model.summary())