import random
from game_data import data
from art import logo, vs

def assign():
    return random.choice(data)

def compare(p1, p2, user_input):
    sum1 = p1['follower_count']
    sum2 = p2['follower_count']

    max_sum = ''
    max_sum = p1['name'] if sum1>sum2 else p2['name']
    return max_sum == user_input

def play_higher_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing = True
        while still_guessing:
            print(logo)
            person1 = assign()
            person2 = assign()
            if score > 0:
                person1 = person2
                person2 = assign()
            print(f"Name: {person1['name']}, Desc: {person1['description']}")
            print(vs)
            print(f"Name: {person2['name']}, Desc: {person2['description']}")
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")
            guess = input("Enter name of person with Higher Followers: ")
            if compare(person1, person2, guess):
                score += 1
            else:
                still_guessing = False


        want_to_play = input("Do you want to play again Higher Lower? (y/n)\n").lower()

        if want_to_play == 'y':
            play_higher_lower()
        elif want_to_play == 'n':
            print("Thanks for playing!")
        else:
            print("Invalid input!.")


if __name__ == '__main__':
    play_higher_lower()

