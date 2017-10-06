#script for Exercise 6: using control structures in python 
#Authors: Melissa Stephens and Janice Love 
#Date: 9-29-2017

import pandas
import matplotlib.pyplot as plt 
import numpy 

data = pandas.read_csv("UWvMSU_1-22-13.txt", delimiter = '\t')

game = numpy.zeros((50,3))
D=pandas.DataFrame(data,columns=['a'])
print D
UW_score = 0
MSU_score = 0

for i in data: #for loop generates final score for each team 
        if data.team[i] == 'UW':
		UW_score = UW_score + data.score[i]        
	elif data.team[i] == 'MSU':
		MSU_score = MSU_score + data.score[i]
	
print UW_score
print MSU_score

plot = plt.plot(data.time,UW_score,'r-',data.time,MSU_score,'g-')

print plot
