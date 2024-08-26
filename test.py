import  random

def getChoices():
    player_choice = input("Enter your choice: (rock, paper, scissor) -> ")
    computer_selection = ["paper", "rock", "scissor"]
    computer_choice = random.choice(computer_selection)
    return checkWhoWin(player_choice, computer_choice)

def checkWhoWin(player, computer):
    print("Player selection --- " + player + " || " + "Computer selection --- " +computer)

    if(player == computer):
        return "Match is tie! "

    elif(player == "rock"):
        if(computer == "scissor"):
            return "Rock smashes the scissor! You win!"
        else:
            return "Paper covers the rock! You lose!"

    elif(player == "paper"):
        if(computer == "rock"):
            return "Paper covers the rock! You Win!"
        else:
            return "Scissor cuts the paper! You lose!"

    elif(player == "scissor"):
        if(computer == "paper"):
            return "Scissor cuts the paper! You Win!"
        else:
            return "Rock smashes the scissor! You win!"

choices = getChoices()
print(choices)



