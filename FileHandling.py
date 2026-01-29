a = "Good Morning bhushan"
b = "How are you?"

# write
# file = open("bhushan.txt", "w")
# file.write(a)
# file.write("\n")
# file.write(b)   


# reads
file = open("bhushan.txt", "r")
# text = file.read()
text = file.readlines()
print(text)

file.close()

print("Successfully written")