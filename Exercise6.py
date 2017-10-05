#Import Stuff
import os
import pandas
import numpy
import matplotlib.pyplot as plt
import random
from random import randint
import scipy
from plotnine import *
#the above may be specific to Windows, I don't remember

#Set Om's WD
#os.chdir('/Users/omneelay/Desktop/Exercise6/Intro_Biocomp_ND_318_Tutorial6/')

#Set JSH WD
os.chdir('C:\\Users\\joshu\\OneDrive\\github\\BioComp\\Tutorial6\\Intro_Biocomp_ND_318_Tutorial6\\')

#CHALLENGE 1
#Import Data
scores=pandas.read_csv("UWvMSU_1-22-13.txt", sep='\t')



#Make dataframe, defined df
#A=scores.time   we may not need this, with a for loop below
#df=pandas.DataFrame(A, columns=['time', 'UWscore', 'MSUscore'])

df=pandas.DataFrame(scores, columns=['time', 'UWscore', 'MSUscore'])
df0=pandas.DataFrame(data=[0,0,0])
df0=df0.T
df0.columns=['time', 'UWscore', 'MSUscore']
frames=[df0,df]
df=pandas.concat(frames)
#this is the list to append to with the loop below
for row in range(0,len(scores)):
#if score is x team, append to x value
#else append to y value
    if scores.iloc[row,1] == "UW": 
        df.iloc[row+1,1] = df.iloc[row,1] + scores.iloc[row,2]
        df.iloc[row+1,2] = df.iloc[row,2]
    elif scores.iloc[row,1] == "MSU":
        df.iloc[row+1,2] = df.iloc[row,2] + scores.iloc[row,2]
        df.iloc[row+1,1] = df.iloc[row,1]
plt.plot(df.time,df.UWscore,'r-',df.time,df.MSUscore,'g-')
#<<<<<<< HEAD
#=======
#dataframe
#for loop to assign score as a float. We need to append to a dataframe, assign scores

#plt.plot("time","UWscore",'r-',"time","MSUscore",'g-')
#so we need to index within the for loop
 
>>>>>>> 28f60eff2feb1aca87958775c080d02ca4866df2



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

