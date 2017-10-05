import pandas
import matplotlib.pyplot as plt

#create a dataframe of raw data
data = pandas.read_csv("UWvMSU_1-22-13.txt", delimiter="\t")

#create a new dataframe to keep running cumulative scores of team over time
total_score = pandas.DataFrame(columns=["time", "UWscore", "MSUscore"])

#setting the time of total_score table with the times from raw data
total_score["time"] = data.time

#Set up running cumulative scores for both teams
total_UW = 0
total_MSU = 0

#Looping through rows of raw data, each row corresponds to the team that scores
for t in range(len(data)):
    #Getting the team that scores at the specified row
    #If the team at that time scores, add score to running total
    if (data.team[t] == "UW"):
        total_UW += data.score[t]
    elif (data.team[t] == "MSU"):
        total_MSU += data.score[t]
        
    #Now fill the corresponding team scores with current running total_score
    total_score.UWscore[t] = total_UW
    total_score.MSUscore[t] = total_MSU
    
#Now plot the linegraph with score vs team score
# -r signifies red line, -g specifies green line
plot = plt.plot(total_score.time,total_score.UWscore, 'r-', total_score.time, total_score.MSUscore, 'g-')


#imports toolbox
import numpy

#initial query
print("I'm thinking of a number between 1 and 100")

#resets loop variable
Q=0

#generates random number
rng=numpy.random.randint(1,high=100,size=1)
rng=int(rng.sum(0))

#user guess
T=int(input("Guess: "))

#loops until correct
while Q==0:
    
    if T<rng:
        print("Higher")
        T=int(input("Guess: "))
    elif T>rng:
        print("Lower")
        T=int(input("Guess: "))
    else:
        print("Correct!")
        Q=1