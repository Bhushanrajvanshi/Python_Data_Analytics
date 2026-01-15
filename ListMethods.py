
# ListMethods

name = ["Bhushan", "Shivam", "Shivansh"]
print(name)
print(name[0])
print(name[1])
print(name[2])
print(type(name))


items = ["Apple", "Banana", "Orange", "Watermelon"]
print(len(items))
items.append("Mango")
# items.append(["Pineapple", "Guava"])
items.extend(["Pineapple", "Guava"])
items.insert(2, "Kiwi")
print(items)
print(items.index("Watermelon"))
print(items.count("Apple"))
items.remove("Watermelon")
print(items)
items.pop(1)  # Remove by index
print(items)
items.clear()  # Clear the list
print(items)  # Empty list


numbers = [1, 6, 2, 8, 3, 9, 4, 88, 22, 55, 22, 77]
numbers.sort()  # Sort the list
print(numbers)
numbers.sort(reverse=True)  # Sort the list in reverse order
print(numbers)
numbers.reverse()  # Reverse the list
print(numbers)
print(88 in numbers)
print(99 in numbers)