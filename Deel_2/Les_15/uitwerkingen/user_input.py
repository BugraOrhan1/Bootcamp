def get_integer(zin):
    while True:
        try:
            user_input = input(zin)
            integer = int(user_input)
            return integer
        except ValueError:
            print('je moet wel een getal invoeren')


def get_float(getal):
    while True:
        try:
            user_input = input(getal)
            float = float(user_input)
            return float
        except ValueError:
            print('je moet wel een getal invoeren')

def get_string(str):
    user_input = input(str)
    return user_input

def get_letter(letter):
    while True:
        user_input = input()
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.upper()
        else:
            print('je moet 1 leter invoeren')

