print("Initializing code......")


# a = int(input("Enter a number: \n")) 
# b = int(input("Enter another number: \n"))

# try : 
#     print("The sum of a/b is", a/b)
# except Exception as e :
#     # print(e) 
#     print("Some Error Occured! - ",e)



try :
    x = int(input("Enter a number: "))
    y = 10 / x
    print(y)
except ValueError : 
    print("please enter a valid number")
except ZeroDivisionError : 
    print("Please enter a number greater than 0")
finally : 
    print("This will always execute")

print("Thank You....")