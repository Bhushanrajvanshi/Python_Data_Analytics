student = {
    "name": "Bhushan",
    "age": 20,
    "branch": "CSE",
    "city": "aurangabad"
}

print(student)
print(type(student))
print(student["name"])
print(student["age"])
print(student["branch"])
# print(student["citiy"])  # Error
print(student.get("city"))

student["city"] = "Patna"
print(student.get("city"))
print(student)