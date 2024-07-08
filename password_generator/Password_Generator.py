import random
import string

def generate_password(length):
    if length < 4:
        print("Length must be greater than or equal to 4")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [random.choice(lower), random.choice(upper), random.choice(digits), random.choice(special)]
    all_characters = lower + upper + digits + special

    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        if password:
            print(f"Your password is: {password}")
    except ValueError:
        print('Please enter a integer.')

if __name__ == '__main__':
    main()

