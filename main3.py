daily_income = [2200, 3850, 4878, 5500, 6000, 7500, 9000, 12000, 15000, 20000]

total = 0 
for income in daily_income: 
    total = total + income
average = total / len(daily_income)
print(f"Средний доход: {average} рублей")

max1 = daily_income[0]
for income in daily_income:     
    if income > max1:
        max1 = income
print(f"макс. доход за день: {max1} рублей")