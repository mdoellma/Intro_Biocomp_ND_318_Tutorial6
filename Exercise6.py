#Import Stuff
import os
import pandas
import numpy
import matplotlib.pyplot as plt
import random
from random import randint

#Set Om's WD
os.chdir('/Users/omneelay/Desktop/Exercise6/Intro_Biocomp_ND_318_Tutorial6/')

#Set JSH WD
#os.chdir('C:\\Users\\joshu\\OneDrive\\github\\BioComp\\Tutorial6\\Intro_Biocomp_ND_318_Tutorial6\\')

#CHALLENGE 1
#Import Data
scores=pandas.read_csv("UWvMSU_1-22-13.txt", sep='\t')

#Set initial scores =0
UWtotalscore=0
MSUtotalscore=0

#Make dataframe
A=scores.time
dataframe=pandas.DataFrame(A, columns=['time', 'UWscore', 'MSUscore'])



#CHALLENGE 2

#Generate Random Number
RandomNumber=randint(1,100)

print ('Im thinking of a number between 1 and 100...')
Guess=int(input("Guess: "))

while Guess != RandomNumber:
    if Guess > RandomNumber:
        print ('Guess:', Guess)
        print ('Lower')
        Guess=int(input("Guess: "))
    elif Guess < RandomNumber:
        print ('Guess:', Guess)
        print ('Higher')
        Guess=int(input("Guess: "))
print ('Guess:', Guess)
print ('Correct!')

