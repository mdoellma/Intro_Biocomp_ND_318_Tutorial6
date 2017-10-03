#change to appropriate directory with unix commands or with 'preferences'
#1 plot generation
#add data
import pandas
import numpy
UWvMSU = pandas.read_csv("UWvMSU_1-22-13.txt",header=0,sep="\t") #read original file with scores
print(UWvMSU)
UWvMSU.shape #number of rows, columns
len(UWvMSU) #length of file
scorearray = numpy.zeros((50,3)) #need time, cumulative score for each team
print(scorearray) #makes an array populated with zeros
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
while guess != random and attempt < random:
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
random=np.random.choice(numbers)
guess= raw_input("I'm thinking of a number between 1-100. Try to guess it:")
while guess != random and guess < random:
    print("Higher")
    guess= raw_input("Guess: ")
elif guess > random:
    print("Higher")
    guess= raw_input("Guess: ")
else:
    print("Correct!)
    
#select all of the following text and run it 
#add packages 
import numpy as np
#how many guesses taken, will be added to
guessesTaken = 0
#make array from 1:100
numbers=range(1,101,1)
#computer assigns random numbers
random=np.random.choice(numbers)
#program asks user name
print('Hello! What is your name?')
myName = raw_input() #user supplies name
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')#let the games begin
while guessesTaken < 100: #runs for 100 guesses, then will terminate
    print('Take a guess.') 
    guess = raw_input() #takes user's first guess
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1 #adds one for each guess
    
    if guess < random: #user's guess too low
        print('Your guess is too low.') 

    if guess > random: #user's guess too high
        print('Your guess is too high.')

    if guess == random: #user's guess correct
        break
if guess == random: #once correct it lets the user know they were correct
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')


