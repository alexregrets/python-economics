monthly_income = [
    15000, 0, 12000, 2200, 0, 11000, 3300,
    0, 22000, 1500, 0, 18000, 2500, 0,
    20000, 3000, 0, 16000, 4000, 0,
    14000, 5000, 0, 19000, 6000, 0,
    17000, 7000, 0, 21000
]

week1 = monthly_income[:7]
week4 = monthly_income[-7:]
every_third = monthly_income[::3]

print("Первая неделя:", week1)
print("Последняя неделя:", week4)
print("Каждый 3-й день:", every_third)