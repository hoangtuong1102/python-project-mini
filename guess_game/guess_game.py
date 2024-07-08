import random

def select_random_words():
    words  = ['python', 'hangman', 'programming', 'developer', 'software']
    return random.choice(words)

def display_words(words, guessed_letters):
    display = ''
    for letter in words:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def play_game():
    word_to_guess = select_random_words()
    guessed_letters = set()
    attempts = 6
    print('WELCOME TO PLAY GUESSING GAME')
    while attempts > 0:
        current_display = display_words(word_to_guess, guessed_letters)
        print(f'Word to guess: {current_display}')
        print(f'Attempts: {attempts}')
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print('You have already guessed that letter')
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print('Good guess')
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print('Incorrect guess.')
        if set(word_to_guess).issubset(guessed_letters):
            print('You have already guessed that letter')
            break
    else:
        print('GAME OVER')

if __name__ == '__main__':
    play_game()