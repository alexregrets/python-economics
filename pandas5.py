import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats



sales = pd.DataFrame({
    "product_id": [101, 102, 103, 104],
    "units": [50, 30, 20, 40]
})

prices = pd.DataFrame({
    "product_id": [101, 102, 105],
    "price": [1000, 1500, 2000]
})


result = pd.merge(sales, prices, on = "product_id", how = "left")
print(result)


