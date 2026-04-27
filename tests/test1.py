def grade(score):
    if score >= 90:
        return "Пиздато"
    if score >= 75:
        return "Нормас"
    if score >= 60:
        return "Так себе"
    if score <= 60:
        return "Залупа"


print("Введите чо получил")
score = int(input())
print(grade(score))


prices = [81.95, 81.70, 81.45, 81.12, 80.85]

summ = 0
for day in prices:
    summ = summ + day
    average = summ / len(prices)

print(f"Сумма за 5 дней: {summ} рублей")
print(f"Средний курс: {average} рублей")



data = [54, 12, 89, 3, 41, 76, 28, 65, 92, 17]

value1 = data[:3]
value2 = data[-3:]
value3 = data[::2]

print(value1)
print(value2)
print(value3)


import pandas as pd


dataa = {
    "day": [1, 2, 3, 4, 5],
    "revenue": [12000, 8000, 15000, 9500, 11000]
}

df = pd.DataFrame(dataa)

