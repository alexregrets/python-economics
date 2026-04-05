import pandas as pd


data = {
    "student": ["Аня", "Боря", "Вася", "Галя", "Дима"],
    "subject": ["math", "english", "math", "english", "math"],
    "hours": [3, 7, 2, 9, 5],
    "income": [3000, 8400, 1600, 9900, 5000]
}

df = pd.DataFrame(data)

# Сгруппируй по предмету, посчитай среднее
print(df.groupby("subject")["income"].mean())

print(df.groupby("subject")["income"].sum())