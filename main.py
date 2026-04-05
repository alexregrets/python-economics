name = input("Как тебя зовут? ")
days_sober = int(input("Дней трезвости: "))
debt = int(input("Долг:"))
hourly_rate = int(input("Почасовая ставка:"))


hours_needed = debt / hourly_rate 

print(f"\nИмя: {name}")
print(f"Дней трезвости: {days_sober}")
print(f"Часов до закрытия долга: {hours_needed:.1f}")
print(f"Это примерно {hours_needed / 2:.0f} сессий по 2 часа")


if days_sober >= 120: 
    print("120 дней выполнено. Условие для марки соблюдено!")
elif days_sober >=30:
    print(f"Хороший прогресс! Осталось {120 - days_sober} дней до 120!")
elif days_sober >= 7:
    print(f"Первая неделя пройдена! Осталось {120 - days_sober} дней до 120!")
else:
    print(f"Критическое окно! До 120 дней осталось {120 - days_sober} ")
    