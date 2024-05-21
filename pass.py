import random
import string


def generate_password(min_lenght, numbers=True, spec_char=True):
    letter = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letter
    if numbers:
        characters += digits
    if spec_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if spec_char:
            meets_criteria = meets_criteria and has_special

    return pwd


min_lenght = int(input("Type min lenght of the password:"))
has_number = input(
    "Do you want ot have numbers in your password y/n :").lower() == 'y'
has_special = input(
    "Do you want to have special characters in yoyr password y/n :").lower() == 'y'
prin = generate_password(min_lenght, has_number, has_special)
print(prin)
