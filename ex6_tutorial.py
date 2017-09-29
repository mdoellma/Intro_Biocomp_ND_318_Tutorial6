#script for Exercise 6: using control structures in python 
#Authors: Melissa Stephens and Janice Love 
#Date: 9-29-2017

f = open('UWvMSU_1-22-13.txt' ,'r')
print f 

import pandas
import matplotlib.pyplot as plt 
import numpy 

data = pandas.read_csv("UWvMSU_1-22-13.txt", delimiter = '\t')

game = numpy.zeros((50,3))

UW_score = 0
MSU_score = 0


for i in range (0, len(data),1): #for loop generates final score for each team 
        if data.team[i] == 'UW':
            UW_score = UW_score + data.score[i]
        elif data.team[i] == 'MSU':
            MSU_score = MSU_score + data.score[i]


D = pandas.DataFrame(game, columns[= ['time', 'team', 'score']) 


for i in range (0,len(data),1):
    D.time[i] == D.time[i]
    if data.team[i]== 'UW':
        D.team[i] = 'UW'
    elif data.team[i] == 'MSU':
        D.team[i] = 'MSU'

        
for i in range (0,len(data),1):
    if i == 0:
        D.score[i] = data.score[i] 
    elif i > 0: 
        D.score[i] = data.score[i] + D.score[i-1]



plot = plt.plot(data.time,UWscore,'r-',data.time,MSUscore,'g-')    
