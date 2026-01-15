# Tuple in python
# Tuple is immutable
# Tuple is ordered
# Tuple is indexed
# Tuple is allows duplicate values

numbers = [1, 4, 7, 8]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

numbers[1] = 10
numbers[3] = 10

print(numbers)

items = ("Apple", "Banana", "Orange", "Watermelon")
print(items)
print(items[-1])
print(len(items))
print(items.count("Apple"))
print(items.index("Watermelon"))

list1 = list(items)
print(list1)

tuple1 = ("Bhushan",)
print(tuple1)