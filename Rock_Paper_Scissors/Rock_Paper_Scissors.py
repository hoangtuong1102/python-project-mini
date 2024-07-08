import random

def get_user_choice():
    user_input = input("Rock, Paper, Scissors!\n").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Please enter rock, paper, or scissors!")
        user_input = input("Rock, Paper, Scissors!\n").lower()
    return user_input

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "paper") \
        or (user_choice == "paper" and computer_choice == "scissors")\
        or (user_choice == "scissors" and computer_choice == "rock"):
        return 'You lose!'
    else:
        return 'You win!'

def play_game():
    print('Welcome to Rock Paper Scissors!')
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print('Your choice {}'.format(user_choice))
    print('Computer choice {}'.format(computer_choice))

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == '__main__':
    play_game()