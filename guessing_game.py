# Random Guessing Game

# importing module for guessing a random number
import random
# range of number
n = 20
# generating a random number
num_guess = int(n * random.random()) + 1
# initialisation
guess =0 
# logic of game
while guess != num_guess:
	guess = int(input("Enter number: "))
	if guess > 0:
		if guess > num_guess:
			print("number is too large")
		elif guess < num_guess:
			print("number is too small")
	else:
		print("You are giving up!!!")
		break
else:
	print("Congrats you made it ")