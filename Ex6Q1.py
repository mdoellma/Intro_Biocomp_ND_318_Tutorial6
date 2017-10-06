#load file
import pandas
data=pandas.read_csv("UWvMSU_1-22-13.txt",header=0,sep="\t")
#making a UW only table
UWscore=data[data.team == 'UW']
#making a MSU only table
MSUscore=data[data.team == 'MSU']
#cumulative sum of UW scores
UWscore['cum_sum'] = UWscore.score.cumsum()
#cumulative sum of MSU scores
MSUscore['cum_sum'] = MSUscore.score.cumsum()
#making a line plot
import matplotlib.pyplot as plt
plt.plot(UWscore['time'], UWscore['cum_sum'], 'r-', MSUscore['time'], MSUscore['cum_sum'], 'g-')

