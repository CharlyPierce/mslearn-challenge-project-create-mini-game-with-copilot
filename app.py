import random
import sys
import signal
#create a function to handle the signal interrupt (ctrl + c) and exit the program
def signal_handler(signal, frame):
    #clean the screen
    print("\033c")
    print("[+] Exit ...")
    sys.exit(0)
#register the signal SIGINT (ctrl + c) to the handler function
signal.signal(signal.SIGINT, signal_handler)



#create function to ask the user to play again and return the user input
def ask_to_play_again(score=0):
    print("\033c")
    print(f"Score: {score}")
    print("Would you like to play again?")
    print("Press 1 to play again")
    print("Press 2 to exit the game")
    user_input = input("What would you like to do? ")
    return user_input

score=None
while True:
    #check the score if is differento to 0, not ask again
    if score == None:
        score = 0
        print("\033c")
        print("Welcome to the game rock, paper, scissors")
        print("Press 1 to start the game")
        print("Press 2 to exit the game")
        user_input = input("What would you like to do? ")
    else:
        user_input = ask_to_play_again(score)

    if user_input == '1':
        #clean the screen
        print("\033c")
        print("Great! Let's start the game")
        print("Press 1 for rock")
        print("Press 2 for paper")
        print("Press 3 for scissors")
        user_choice = input("What would you like to choose? ")

        if user_choice == '1':
            user_choice = "rock"
        elif user_choice == '2':
            user_choice = "paper"
        elif user_choice == '3':
            user_choice = "scissors"
        else:
            print("Invalid input, please try again")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"You choose {user_choice}, computer choose {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "paper":
            print("You lose!")
            #less 1 point to the score
            score -= 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
            #add 1 point to the score
            score += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            #add 1 point to the score
            score += 1
        elif user_choice == "scissors" and computer_choice == "rock":
            print("You lose!")
            #less 1 point to the score
            score -= 1
        elif user_choice == "paper" and computer_choice == "scissors":
            print("You lose!")
            #less 1 point to the score
            score -= 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            #add 1 point to the score
            score += 1
        input("press enter to continue")
        

    elif user_input == '2':
        print("See you next time!")
        break
    else:
        print("Invalid input, please try again")
        input("press enter to continue\n")
        score == None
        continue   
