#change to appropriate directory with unix commands or with 'preferences'
#1 plot generation



#2 GAME: GUESS MY Number Vs 1
#add packages
import numpy as np
#select code from here to break to run game
#make array from 1:100
numbers=range(1,101,1)
#computer assigns random numbers
random=np.random.choice(numbers)
#set number outside of range so that the first loop works
guess=0
print("I'm thinking of a number between 1-100. Try to guess it.")
while guess != random:
    guess=raw_input('Guess:') #gives prompt
    guess=int(guess) #converts guess to integer
    if guess < random: #if guess is too low
        print('Guess:' + str(guess))
        print("Higher")
    elif guess > random: #if guess is too high
       print('Guess:'+ str(guess))
       print("Lower")
    else: #if guess is correct
        print('Guess:'+ str(guess))
        print("Correct! " + str(guess))
        break #ends the loop

#GAME Guess my Number Vers. 2.0 (also asks name and says number of guesses)
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
        print('Your guess, ' + str(guess) + ', is too low.') 

    if guess > random: #user's guess too high
        print('Your guess, ' + str(guess) + ', is too high.')

    if guess == random: #user's guess correct
        break
if guess == random: #once correct it lets the user know they were correct
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number, ' + str(guess) + ', in ' + guessesTaken + ' guesses!')
#game complete at this point

