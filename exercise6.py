#change to appropriate directory with unix commands or with 'preferences'
#1 plot generation
#add data
import pandas
import numpy
#Columns in final array: 1st is time, 2nd is MSU score, 3rd is UW score
UWvMSU = pandas.read_csv("UWvMSU_1-22-13.txt",header=0,sep="\t") #read original file with scores, tabs are delimeter
scorearray = numpy.zeros((51,3)) #this is the new array that I am going to populate with data, there is an extra row at the top so time zero is zero score
for row in range(0,len(UWvMSU),1): #starting with row zero through the length of the original file (UWvMSU), counting by 1, variable is "row"
    scorearray[row+1,0] = UWvMSU.iloc[row,0] #in row+1 (starting with second row b/c first row is zero), populate column 1 of scorearray (index zero) with times from column 1 in UWvMSU data
    if UWvMSU.iloc[row,1] == "MSU": #read through rows in column 2 (index 1) in UWvMSU, see if it reads MSU
        scorearray[row+1,1] = scorearray[row,1] + UWvMSU.iloc[row,2] #populate the scorearray with row+1(the next row, in column 2,(index 1) and add the score from UWvMSU file with row and score from UWvMSU
        #part above is for adding cumulative score for MSU
        scorearray[row+1,2] = scorearray[row,2] #populate the third column (index 2) of scorearray with the score from column 3 (index 2) without adding to the score
        #cumulative score for UW above, doesn't add to score when MSU is found
    else: #this assumes no errors and that anything besides MSU will be UW 
        scorearray[row+1,2] = scorearray[row,2] + UWvMSU.iloc[row,2] #in reverse of the first part of the if statement, add to the culmulative score for UW
        scorearray[row+1,1] = scorearray[row,1] #don't add to the score for MSU, move the last score down to the next row
print(scorearray) #a print step for checking the array for cumulative scores, I may hash it out later


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


