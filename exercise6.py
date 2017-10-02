#change to appropriate directory with unix commands or with 'preferences'
#1 plot generation
#add data

#add packages
import matplot.pyplot as plt


#2 game (guess my number)
#add packages
import numpy as np
#make array from 1:100
numbers=range(1,101,1)
#computer assigns random numbers
random=np.random.choice(numbers)
guess= raw_input("I'm thinking of a number between 1-100. Try to guess it:")
attempt= 0
while guess != random and guess < random:
    print("Higher")
    guess=raw_input("Guess: ")
    attempt= guess
if attempt==random:
    print("Correct!")
elif attempt < random:
    print("Higher")
else:
    print("Lower")
#check http://www.openbookproject.net/books/bpp4awd/ch04.html
#or https://wiki.python.org/moin/WhileLoop

##attempt # 2
#