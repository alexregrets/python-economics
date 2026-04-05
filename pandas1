import pandas as pd

data = {
    "day": list(range(1, 31)),
    "income": [15000, 0, 12000, 2200, 0, 11000, 3300,
               0, 22000, 1500, 0, 18000, 2500, 0,
               20000, 3000, 0, 16000, 4000, 0,
               14000, 5000, 0, 19000, 6000, 0,
               17000, 7000, 0, 21000]
}

df = pd.DataFrame(data)
print(df.head())
print("\nСредний доход:", df["income"].mean())
print("Максимум:", df["income"].max())

def income_status(income):
    if income == 0:
        return "Weekend"
    elif income < 5000:
        return "Low"
    elif income < 15000:
        return "Avg"
    else:
        return "High"
    
df["status"] = df["income"].apply(income_status)
high_days = df[df["income"]>10000]



print("\nТаблица со статусами(первые 10 строк):")
print(df.head(10))
print("\nДни с доходом > 10000:")
print(high_days[["day","income", "status"]])
print(df.shape)   
    




