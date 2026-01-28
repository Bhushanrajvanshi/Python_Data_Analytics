student = {
    "name": "Bhushan",
    "age": 20,
    "city": "aurangabad"
}

print(student)

student["Branch"] = "CSE"
print(student)

student.popitem()
print(student)

# del student["city"]
# print(student)

# student.clear()
# print(student)

# print(len(student))

print(student.keys())
print(student.values())
print(student.items())
