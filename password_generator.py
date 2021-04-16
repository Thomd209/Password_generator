from string import printable
from random import randint

password_chars = []  # Symbols that the generated password can contain
# Filling the list with symbols
for i in range(len(printable)):
    password_chars.append(printable[i])

password_length = int(input())  # Length of password
random_char = 0  # Number of randomly generated character
password = ''  # Generated password
# Filling the password with random characters
for i in range(password_length):
    random_char = randint(0, len(password_chars) - 1)
    password += password_chars[random_char]

print(password)
