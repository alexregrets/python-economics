student = {
    "name": "Alex",
    "age": 20,
    "gpa": 73,
    "city": "Moscow",
    "debt" : 29000
}

print(student["name"])
print(student["gpa"])
print(student["debt"])

print(student.keys())
print(student.values())
print(student.items())


#for key, value in student.items():
 #   print(f"{key}: {value}")


for key, value in student.items():
    if type(value) == int:
        print(f"{key}: {value}")




def sum_numbers(d):
    sum = 0
    for key, value in d.items():
        if type(value) == int:
            sum = sum + value
    return sum




data = {"city": "Moscow", "income": 5500, "students": 2, "language": "Russian"}
print(sum_numbers(data))