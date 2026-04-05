
def sobriety_status(days):
    """Возвращает статус прогресса трезвости"""
    if days >= 120:
        return "Цель достигнута"
    elif days >= 30:
        return "Серьёзный прогресс"
    elif days >= 7:
        return "На верном пути"
    else:
        return "Критическое окно"

def debt_status(debt, hourly_rate):
    if debt <= 0:
        return "Долг закрыт"
    if debt/hourly_rate < 10:
        return "Срочно"
    if debt/hourly_rate < 50:
        return "Норм"
    else:
        return "Долго"




# Основная программа
name = input("Как тебя зовут? ")
days_sober = int(input("Дней трезвости: "))
debt = int(input("Долг (руб): "))
hourly_rate = int(input("Ставка (руб/час): "))

hours_needed = debt / hourly_rate
sessions_needed = hours_needed / 2

print(f"\n=== Результат ===")
print(f"Имя: {name}")
print(f"Дней трезвости: {days_sober}")
print(f"Статус: {sobriety_status(days_sober)}")
print(f"Часов до закрытия долга: {hours_needed:.1f}")
print(f"Сессий по 2 часа: {sessions_needed:.0f}")
print(f"Статус долга: {debt_status(debt, hourly_rate)}")
