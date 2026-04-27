employees = [
    {"name": "Alex", "salary": 50000, "city": "Moscow"},
    {"name": "Anya", "salary": 80000, "city": "SPb"},
    {"name": "Bogdan", "salary": 65000, "city": "Kazan"}
]


#for employee in employees:
    #print(employee['name'], employee['salary'])




def mean_salary(employees):
    total_salary = 0 
    for employee in employees:
        total_salary = total_salary + employee['salary']
    return total_salary / len(employees)

print(mean_salary(employees))


salaries = [e["salary"] for e in employees]
print(sum(salaries) / len(salaries))


names = [n['name'] for n in employees]
print(names)