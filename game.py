import random

#import modules 




#options for the game




#start the game
print("Welcome to Rock, Paper, Scissors!")
userChoice = input("Type in your choice: ") 

i = 1
while i < 4:
    print(i)
    i += 1

options = ["rock", "paper", "scissors"] 

computerChoice = random.choice(options)

print(computerChoice)




#logic of the game





def outcome():
    if computerChoice == options[0] and userChoice == options[0]:
        return "it's a tie!"
    elif computerChoice == options[0] and userChoice == options[1]:
        return "You won!"
    elif computerChoice == options[1] and userChoice == options[0]:
        return "You won!"
    elif computerChoice == options[0] and userChoice == options[2]:
        return "I won!"
    elif computerChoice == options[2] and userChoice == options[0]:
        return "I won!"
    elif computerChoice == options[2] and userChoice == options[1]:
        return "I won"
    elif computerChoice == options[1] and userChoice == options[2]:
        return "I won"
    elif computerChoice == options[2] and userChoice == options[2]:
        return "It's a tie!"
    elif computerChoice == options[1] and userChoice == options[1]:
        return "It's a tie!"
print(outcome()) 










