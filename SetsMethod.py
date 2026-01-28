items = {"apple", "banana"}
items.add("orange")
print(items)

items.update(["mango", "kiwi"])
print(items)

items.remove("apple")   # Remove by value
# items.remove("applee")     # Error
print(items)

items.discard("banana")     # No error
print(items)

items.clear()
print(items)




a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.union(b)
print(result)

result = a.intersection(b)
print(result)