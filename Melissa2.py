import random

user_input=raw_input("guess my number\n")
N= random.randint(1,100)
print N

guess=0

while guess !=N:
	guess= int
	if guess > 0:
		if guess > N:
			print ("Lower")
		elif guess < N:
			print ("Higher")
else:
	print "Correct!"
	


