# Analysis for Tutorial 6


# Set working directory
os.chdir('/Users/brittnibertolet/Desktop/bcTutorials/Intro_Biocomp_ND_318_Tutorial6/')

# Load packages
import numpy 
import pandas
from plotnine import *

############################################
################ Question 1 ################
############################################
# Read in data
game=pandas.read_csv("UWvMSU_1-22-13.txt",sep="\t",header=0)

# Subset the two teams into different dataframes
MSU=game[game['team']=="MSU"]
UW=game[game['team']=="UW"]

# Calculate cummulative score at each time for MSU
MSU['cum']=0 # make column to fill with cummulative score
position=pandas.Series(range(1,27)) # make set of indexes
MSU.iloc[0,3]=MSU.iloc[0,2] # assign the first value
for i in position:
    MSU.iloc[i,3]=MSU.iloc[i,2] + MSU.iloc[i-1,3] # loop to add everything up

# Calculate cummulative score at each time for UW
UW['cum']=0 # make column to fill with cummulative score
position=pandas.Series(range(1,23)) # make set of indexes
UW.iloc[0,3]=UW.iloc[0,2] # assign the first value
for i in position:
    UW.iloc[i,3]=UW.iloc[i,2] + UW.iloc[i-1,3] # loop to add everything up

# Create plot with UW in red and MSU in green
import matplotlib.pyplot as plt
plt.plot(UW.iloc[0:,0],UW.iloc[0:,3],'r-',MSU.iloc[0:,0],MSU.iloc[0:,3],'g-')

############################################
################ Question 2 ################
############################################






