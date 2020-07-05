print('This is a guessing game')
import random
random_number = random.randrange(1,10)
guess = int(input("What could be the number?"))
correct = False
print(random_number)

while not correct:
	if guess==random_number:
		print("Congrats you got it")
		correct=True
	elif guess>random_number:
		print("To high")
		break

	elif guess<random_number:
		print("To low")
		break
	else:
		print("Try something else")
		break