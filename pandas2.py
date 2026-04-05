

import pandas as pd
data = {
    "student": ["Aня", "Боря", "Вася", "Галя", "Дима"],
    "hours": [3, 7, 2, 9, 5],
    "rate": [1000, 1200, 800, 1100, 1000]
}

df = pd.DataFrame(data)

df[df["hours"] > 4]
print(df[df["hours"] > 4])

df["income"] = df["hours"] * df["rate"]

print(df)

print(df["income"].mean())

print(df.iloc[1, 2])

print(df.iloc[1:4, 0:2])
print(df.loc[2, "student"])