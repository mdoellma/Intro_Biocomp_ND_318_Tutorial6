"""
Exercise 6 Challenge question 2
Kathleen Nicholson and Grant Keller
######
A fun game with random numbers in Python.
8.1/10 - critics raved:
"Reminds me of that game with the portals. What was it called again?" - Emeril Lagasse
"Better replay value than Cooking Mama!" - Sarah Huckabee Sanders
"Who are you and what are you doing here?" - Lance M. Hellman
"""

from __future__ import print_function
from random import randint, choice
from time import sleep


def zalgo(text, intensity=50):
    """
    This and the following 2 functions are from PyZalgo module
    (https://github.com/mjgiarlo/pyzalgo/blob/master/zalgo.py)
    and included here to simply use in grading.
    """
    zalgo_threshold = intensity
    zalgo_chars = [unichr(i) for i in range(0x0300, 0x036F + 1)]
    zalgo_chars.extend([u'\u0488', u'\u0489'])
    source = text.decode('utf8').upper()
    if not _is_narrow_build:
        source = _insert_randoms(source)
    zalgoized = []
    for letter in source:
        zalgoized.append(letter)
        zalgo_num = randint(0, zalgo_threshold) + 1
        for _ in range(zalgo_num):
            zalgoized.append(choice(zalgo_chars))
    response = choice(zalgo_chars).join(zalgoized)
    return response.encode('utf8', 'ignore')
def _insert_randoms(text):
    random_extras = [unichr(i) for i in range(0x1D023, 0x1D045 + 1)]
    newtext = []
    for char in text:
        newtext.append(char)
        if randint(1, 5) == 1:
            newtext.append(choice(random_extras))
    return u''.join(newtext)
def _is_narrow_build():
    try:
        unichr(0x10000)
    except ValueError:
        return True
    return False

if __name__ == "__main__":
    # Intro text. Module uses sleep() function for enthusiastic timing
    #   of otherwise boring text.
    print("\nHello and, again, welcome to the Aperture Science computer-aided enrichment center.")
    sleep(1.5)
    print("We hope your brief detention in the relaxation vault has been a pleasant one.")
    sleep(2)
    # determines pseudo-random number using builtin library
    COMPUTER_NUM = randint(0, 101)
    # sets user_number to an illegitimate (in-game) value
    USER_NUM = -10
    # PEP 8 specifications have line length limits (100 char).
    #   For this reason, we have opted to use the end argument
    #   to keep lines manageable, if overused.
    print("\nNo one will blame you for giving up.", end=' ')
    print("In fact, quitting at this point is a", end=' ')
    print("perfectly reasonable response.", end=' ')
    sleep(2)
    print("You can exit the test at any time by entering 'q' or 'quit'.")
    sleep(3)
    print('\n')
    while USER_NUM != COMPUTER_NUM:
        # i.e. user has not guessed the random number
        USER_NUM = raw_input("Guess a number between 1 and 100: ")
        # provides a way to end the game manually
        if USER_NUM == 'q' or USER_NUM == 'quit':
            break
        try:
            USER_NUM = int(USER_NUM)
        except ValueError:
            # i.e. user number is not an integer
            try:
                # check if user number is type float and can be
                #   (crudely) converted to an int. Number is rounded incorrectly
                #   to frustrate user.
                USER_NUM = int(round(float(USER_NUM))) + randint(-6, 6)
                MSG = ["You", " gave", " me", " a {}?!".format(zalgo("decimal", 1))]
                for i in range(4):
                    sleep(0.3)
                    print(MSG[0], end='')
                sleep(0.5)
                for i in range(1, 4):
                    sleep(0.8)
                    print(MSG[i], end='')
                sleep(1)
                print('\n')
                print("Executing", end=' ')
                sleep(0.5)
                print(zalgo("low-accuracy", 1), end=' ')
                sleep(0.5)
                print(zalgo("rounding", 2), end=' ')
                sleep(0.5)
                print(zalgo("protocol", 3), end=' ')
                for i in range(4):
                    sleep(1.5)
                    print('.', end='')
                print('\n')
            except ValueError:
                # User number is not real or NaN or something else, I guess.
                #   At this point, they need to simply try again.
                print("\nI certainly expected more from you.")
                sleep(1)
                print("Please try again with a real number,", end=' ')
                print('not "{}".'.format(USER_NUM))
                sleep(2)
                continue
        if USER_NUM > 100 or USER_NUM < 1:
            # User number is out of bounds.
            print("\nI give you a score of 3.4 for style and 10 for being annoying.")
            print("Try again, but only between 1 and 100 inclusive,", end=' ')
            print("which does not include {}.".format(USER_NUM))
            sleep(4)
            continue
        elif USER_NUM > COMPUTER_NUM:
            # Reminds user of input and informs them that they're too high.
            print("\nResults of this test were highly informative.")
            sleep(2)
            print("Too highly. Try a number lower than {}.".format(USER_NUM))
            sleep(4)
        elif USER_NUM < COMPUTER_NUM:
            # Reminds user of input and informs them that they're too low.
            print("\nThat's a low bar, but you managed", end=' ')
            print("to gently tip-toe under it.")
            sleep(2)
            print("Try another number, higher than {}.".format(USER_NUM))
            sleep(4)
    if user_number[0] != 'q':
        # If while loop is broken, but user did not manually quit, play winning
        #   message - we don't congratulate quitters here, Dave.
        print("Test chamber completed. In the interest of science,", end=' ')
        print("the Enrichment Center proudly presents the following list", end=' ')
        print("of numbers: Nine. Seven. Fifty. Three. Seven hundred and seven.")
        sleep(5)
