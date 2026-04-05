


daily_income = 1100 * 2 
total = 0 
for day in range (1, 31): 
    total = total + daily_income 
    if day % 10 == 0:
        print(f"День {day}: накоплено {total} руб.")

print(f"Итого за 30 дней: {total} руб.")
print(f"Долг закрыт: {total >= 30000}")