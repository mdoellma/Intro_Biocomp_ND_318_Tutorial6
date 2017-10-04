# Using control structures in Python
# Authors: Grant Keller and Kathleen Nicholson
"""
TO-DO:

1. Label x axis.
2. Label y axis.
3. Include legend.
4. Title the plot.
5. Maybe add gridlines? This could make it more informative.
6. Comment this code after (see Q2 for examples).
"""


import pandas
import matplotlib.pyplot as plt
#Q1

UWvMSU = pandas.read_csv('UWvMSU_1-22-13.txt', sep='\t')
UW_score = [0]
MSU_score = [0]
time = [0]
for i in range(0, UWvMSU.shape[0], 1):
    if UWvMSU.team[i] == 'UW':
        UW_score.append(UW_score[-1]+UWvMSU.score[i])
        MSU_score.append(MSU_score[-1])
    elif UWvMSU.team[i] == 'MSU':
        MSU_score.append(MSU_score[-1]+UWvMSU.score[i])
        UW_score.append(UW_score[-1])
    time.append(UWvMSU.time[i])
plt.plot(time, UW_score, 'r-', time, MSU_score, 'g-')