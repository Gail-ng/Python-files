#programme to demonstrate a game rock, paper,scisssors
#rules of the game rock,paper,scissors
print(".......Welcome to the Rock Paper Scissors game\n"
      "Please take note of the following winning rules: \n"
      
                                +"Rock vs Paper->paper wins \n"
                                + "Rock vs Scissor->Rock wins \n"
                                +"Paper vs Scissor->Scissor wins \n"
                                +"you are expected to choose R for Rock, P for Paper, S for Scissors\n")

print(".......expected action\n")
user_name=input("Please enter your name. >")

  #List Choices
possible_action=["R","P","S"]
print("Game Choices", possible_action)
print("\n R -- Rock \n P-- Paper \n S --Scissors")

import random

while True:

    # Allow player/user make input
    user_action=input("enter a choice(R,P,S):\n")
    possible_action=["R","P","S"]

    #Computer picks a random choice from the list above
    computer_action= random.choice(possible_action)
    print (f"\nYou choose {user_action} computer choose {computer_action}.\n")

    #programme to determine the outcome of the game
    if user_action==computer_action:
        print(f"both players selected {user_action}.It is a tie!")
    elif user_action=="R":
        if computer_action=="S":
            print("Rock smashes Scissors! You win!")
        else:
            print("Rock smashes Scissors! computer lose!")
            
    elif user_action=="P":
        if computer_action=="R":
            print("Paper covers rock! You win")
        else:
            print("Paper covers rocK! Computer lose.")
            
    elif user_action=="P": 
        if computer_action=="S":
            print("Scissors cuts paper! You lose!")
        else:
            print("Paper covers Scissors! computer wins!")
            

    #checking an unidentified choice made by a player 
    elif [False, False, False]==[user_action == choice for choice in possible_action]:
       print("Input Error!\n Please input 'R','P' or 'S'.\n Try again!")       
 

    play_again=input("Play again?(yes/no):")
    if play_again.lower() =="no":
       print("bye")
       break