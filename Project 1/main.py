import random
'''
2 for snake
-2 for water 
0 for gun
'''
computer = random.choice([-2, 0, 2])
youstr = input("Enter your choice: ")
youDict = {"s": 2, "w": -2, "g": 0}
reverseDict = {2: "Snake", -2: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-2 and you == 2): 
        print("You win!")

    elif(computer ==-2 and you == 0):
        print("You Lose!")

    elif(computer == 2 and you == -2):
        print("You lose!")

    elif(computer ==2 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -2):
        print("You Win!")

    elif(computer == 0 and you == 2):
        print("You Lose!")

    else:
        print("Something went wrong!")