import numpy
import pandas
random = numpy.random.choice(range(1,101))
guess = int(input("Guess: "))
while guess <= 100:
    print ("Guess: ",guess)
    if guess > random:
        print ("Lower")
        guess = int(input("Guess: "))
    elif guess < random:
        print ("Higher")
        guess = int(input("Guess: "))
    else:
        print ("Correct!")
        break
