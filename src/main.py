# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
UPPERCASE = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
LOWERCASE = list('abcdefghijklmnopqrstuvwxyz')
NUMBER = list('0123456789')



def generate_password():

    password = []
    length = random.randrange(8,17)
    random.shuffle(NUMBER)
    random.shuffle(SYMBOLS)
    random.shuffle(UPPERCASE)
    random.shuffle(LOWERCASE)
    password.append(random.choice(UPPERCASE))
    password.append(random.choice(LOWERCASE))
    password.append(random.choice(NUMBER))
    password.append(random.choice(SYMBOLS))
    length  = length - 4
    while length > 0:
        choiceList = random.randrange(1,5)
        if choiceList == 1:
            password.append(random.choice(UPPERCASE))
        elif choiceList == 2:
            password.append(random.choice(LOWERCASE))
        elif choiceList == 3:
            password.append(random.choice(NUMBER))
        elif choiceList == 4:
            password.append(random.choice(SYMBOLS))
        length -= 1
    strpassword = "".join(password)
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
