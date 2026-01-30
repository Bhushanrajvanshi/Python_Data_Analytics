import random

def game(user, computer) :
    if user == computer :
        return None
    # snake and water
    if user == "s" and computer == "w" :
        return True
    if user == "w" and computer == "s" :
        return False

    # water and gun
    if user == "w" and computer == "g" :
        return True
    if user == "g" and computer == "w" :
        return False
        
    # gun and snake
    if user == "g" and computer == "s" :
        return True
    if user == "s" and computer == "g" :
        return False
    

randomNum = random.randint(1, 3)

print("Computer's Turn: Snake(s), Gun(g), Water(w)")
if randomNum == 1 :
    computer = "s"
elif randomNum == 2 :
    computer = "w"
else :
    computer = "g"

user = input("Your Turn: Snake(s), Gun(g), Water(w) : ").lower()

result = game(user, computer)       # Function Return true if you win otherwise false
print("You choose : ", user)
print("Computer choose : ", computer)

if result == None :
    print("Draw")
elif result :
    print("You Win")
else :
    print("You Lose")

# print(randomNum)