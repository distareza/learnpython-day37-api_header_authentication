# HashKey Generator Project

from random import *


def hashkey_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [choice(letters) for _ in range(randint(4, 20))]
    password_numbers = [choice(numbers) for _ in range(randint(4, 20))]

    char_list = password_letters + password_numbers

    shuffle(char_list)

    hashkey = "".join(char_list)
    return hashkey


print(f"Your HashKey is: {hashkey_generator()}")