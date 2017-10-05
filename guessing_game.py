#imports toolbox
import numpy

#initial query
print("I'm thinking of a number between 1 and 100")

#resets loop variable
Q=0

#generates random number
rng=numpy.random.randint(1,high=100,size=1)
rng=int(rng.sum(0))

#user guess
T=int(input("Guess: "))

#loops until correct
while Q==0:
    
    if T<rng:
        print("Higher")
        T=int(input("Guess: "))
    elif T>rng:
        print("Lower")
        T=int(input("Guess: "))
    else:
        print("Correct!")
        Q=1