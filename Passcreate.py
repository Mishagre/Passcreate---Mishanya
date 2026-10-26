import random
import string

print("Hello! I am a beginner programmer in Python. I wanted to create my own mini GitHub project, so I finished this! A password creator!")

user_input = input("Enter your length of password (4-10): ")

try:
    length = int(user_input)
except ValueError:
    print(f"{user_input}: not valid, enter a valid length (4-10)")
else:
    if 4 <= length <= 10:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Your password is:", password)
    else:
        print(f"{length}: not valid, enter a valid length (4-10)")
