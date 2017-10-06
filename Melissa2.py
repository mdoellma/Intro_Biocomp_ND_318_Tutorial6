import random

user_input=raw_input
N= random.randint(1,100)

print ("I'm thinking of a number 1-100...(choose 0 to give up)")
while user_input !=N:
	user_input= int(input("Guess:"))
	if user_input > 0:
		if user_input > N:
			print ("Lower")
		elif user_input < N:
			print ("Higher")
	else:
		print ("Giving up? The secret number is:")
		print N
else:
	print "Correct!"
	


