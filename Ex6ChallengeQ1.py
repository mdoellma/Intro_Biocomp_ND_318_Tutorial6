# Using control structures in Python
# Authors: Grant Keller and Kathleen Nicholson
"""
TO-DO:

1. Label x axis. --DONE
2. Label y axis. --DONE
3. Include legend. --DONE
4. Title the plot. --DONE
5. Maybe add gridlines? This could make it more informative. --DONE
6. Comment this code after (see Q2 for examples). --DONE
"""


import pandas
import matplotlib.pyplot as plt
#Q1
#Creates UWvMSU csv as a variable.
UWvMSU = pandas.read_csv('UWvMSU_1-22-13.txt', sep='\t')
#This sets the scores of each team and time as variables equal to zero to begin.
UW_score = [0]
MSU_score = [0]
time = [0]
#This for loop runs through each row and appends zero to the nonscoring team's cumulative score and appends the points earned to the scoring team's
#     cumulative score
for i in range(0, UWvMSU.shape[0], 1):
    if UWvMSU.team[i] == 'UW':
        UW_score.append(UW_score[-1]+UWvMSU.score[i])
        MSU_score.append(MSU_score[-1])
    elif UWvMSU.team[i] == 'MSU':
        MSU_score.append(MSU_score[-1]+UWvMSU.score[i])
        UW_score.append(UW_score[-1])
    time.append(UWvMSU.time[i])
#This plots the cumulative scores as they are added over time and makes the UW score the red line and the MSU score the green line.
plt.plot(time, UW_score, 'r-', time, MSU_score, 'g-')
#This adds the figure legend with corresponding colors. 
plt.legend(('UW', 'MSU',))
#This titles the plot and gives the x and y axis labels. 
plt.title("UW vs. MSU Game Score")
plt.xlabel("time (s)")
plt.ylabel("score")
#This adds gridlines to the plot
plt.grid(True)


