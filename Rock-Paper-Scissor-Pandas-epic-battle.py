import random
import pandas as pd

def user_choice():
    user = input("chose and type either Rock, Paper or Scissors \n \
    if you want to end the game, type Stop ")
    return user

user = ""
#result = ""
computer = ""
list_of_words = ["Rock", "Paper", "Scissors", "Stop"]
list_of_results = []

def computer_choice():
    x = random.randint(1,3)
    if x == 1:
        computer = "Rock"
    elif x ==2:
        computer = "Paper"
    elif x ==3:
        computer = "Scissors"
    return computer

def battle_result():
    if user == computer :
        result = "Draw"
    elif user == "Rock" and computer == "Paper" :
        result = "Computer won"
    elif user == "Paper" and computer == "Rock" :
        result = "You won"
    elif user == "Scissors" and computer == "Rock" :
        result = "Computer won"
    elif user == "Rock" and computer == "Scissors" :
        result = "You won"
    elif user == "Paper" and computer == "Scissors" :
        result = "Computer won"
    elif user == "Scissors" and computer == "Paper" :
        result = "You won"
    return result

while not user in list_of_words:
    user = user_choice()
    
while not user == "Stop":
    computer = computer_choice()
    result = battle_result()
    list_of_results.append(result)
    df = pd.DataFrame(list_of_results,columns=['Results'])
    print("\nYou choose {} and computer choose {} so: \n{} \n".format(user, computer, result))
    print("Overall result: \n{}".format(df['Results'].value_counts()))
    user = user_choice()
    if user not in list_of_words:
        print("type again either Rock, Paper, Scissor or Stop")
        while not user in list_of_words:
            user = user_choice()

print("\nFinal result of the battle: \n{}".format(df['Results'].value_counts()))