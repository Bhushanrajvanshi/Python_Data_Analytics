# def greet() :
#     print("Good Morning")
#     print("How are you?")
#     print("Thank you!")
    
# greet()
# greet()


# def greet(name) :
#     print("Good Morning", name)
#     print("How are you?")
#     print("Thank you!")

# greet("Bhushan")


# def greet(FirstName, lastName) :
#     print("Good Morning", FirstName, lastName)
#     print("How are you?")
#     print("Thank you!")

# greet("Bhushan", "Rajvanshi")


def add(a, b) :
    c = a + b
    return c

sum = add(10, 20)
print(sum)


def func(name="", city="Aurangabad") : 
    print("Hi I Am ", name, "From", city)

func()
func("Bhushan", "Patna")
func(city="Delhi", name="Rajvanshi")



# lambda function
add = lambda a, b : a + b
sum = add(40, 20)
print(sum)