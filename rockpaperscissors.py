from random import randint

#possible choice and win conditions
options = ["rock", "paper", "scissors"]
winCons = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
repeat = True

#Loop until player requests to stop
while repeat:
    playerChoice = ''
    question = 'a' #Holds whether player wants to repeat

    #Get the players choice
    while playerChoice not in options:
        playerChoice = input("What would you like to play?(Rock/Paper/Scissors)\n").lower()
        if playerChoice not in options:
            print("Please choose either Rock, Paper or Scissors\n")

    #Generate computer response with randint
    compChoice = options[randint(0,2)]

    #Find out who wins
    print(f"\nComp choice: {compChoice}, Player choice: {playerChoice}\n")
    if playerChoice == winCons[compChoice]:
        print("you lose, you got beaten by a randomly generated answer... you suck\n")
    elif compChoice == winCons[playerChoice]:
        print("Ok you win, grats\n")
    else:
        print("No one wins\n")

    #ask if player wants to repeat
    while question.lower()[0] not in 'yn':
        question = input("Would you like to play again?(y/n)")

    if question.lower()[0] == 'n':
        repeat = False
