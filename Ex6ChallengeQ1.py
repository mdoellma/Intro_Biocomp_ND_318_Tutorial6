"""
Makes a fun and informative plot from the score/time info provided for us.
UW vs. MSU, 01/22/13.
Authors: Grant Keller and Kathleen Nicholson
"""


import pandas
import matplotlib.pyplot as plt
# Q1
# Reads in UWvMSU txt file as pandas dataframe
UWvMSU = pandas.read_csv('UWvMSU_1-22-13.txt', sep='\t')
# Instantiates list to hold time & score variables, sets first point at 0.
UW_score = [0]
MSU_score = [0]
time = [0]
# Runs through each row and appends zero to the nonscoring team's cumulative score
#   and appends points earned to the scoring team's cumulative score
for i in range(0, UWvMSU.shape[0], 1):
    if UWvMSU.team[i] == 'UW':
        UW_score.append(UW_score[-1]+UWvMSU.score[i])
        MSU_score.append(MSU_score[-1])
    elif UWvMSU.team[i] == 'MSU':
        MSU_score.append(MSU_score[-1]+UWvMSU.score[i])
        UW_score.append(UW_score[-1])
    time.append(UWvMSU.time[i])
# Plots the cumulative scores as they are added over time and makes the UW score a red line and the MSU score a green line.
plt.plot(time, UW_score, 'r-', time, MSU_score, 'g-')
# Adds the figure legend with corresponding colors. 
plt.legend(('UW', 'MSU',))
# Titles the plot, gives the x and y axis labels. 
plt.title("UW vs. MSU Game Score")
plt.xlabel("time (s)")
plt.ylabel("score")
# Adds gridlines to the plot
plt.grid(True)


