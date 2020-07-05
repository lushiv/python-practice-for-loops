print('Welcome to Nepal Bank')
restart = ('Yes')
chances = 4
balance = 9000
while chances >=0:
	pin=int(input("Please enter your 4 didgit pin"))
	if pin == (1415):
		print('You entered your pin correctly\n')
		while restart not in ('n', 'NO' ,'no', 'N'):
			print("Please press 1 for your balance\n")
			print("Please press 2 for your withdrawl\n")
			print("Please press 3 for your pay in\n")
			print("Please press 4 for your return card\n")
			option = int(input("What would you like to choose?"))
			if option==1:
				print('Your balance is $', balance, '\n')
				restart = input('would you like to go back?')
				if restart in ('n', 'NO' ,'no', 'N'):
					print('Thank you for banking with Nepal')
					break
			elif option ==2:
				option2 = ('Yes')
				withdrwal = float(input('How much would you like to withdrwal? \n$10/$20/$30/$40/$50 for other enter 1 '))
				if withdrwal in [10,20,30,40,50]:
					balance = balance-withdrawl
					print('\nYour balance is now $', balance)
					restart = input('What would you like to do')
					if restart in ('n', 'No', 'no', 'N'):
						print('Thank you for banking with Nepal bank')
						break
					elif withdrwal != [10,20,30,40,50]:
						print('Invalid amount, please re-try\n')
						restart=('Yes')
					elif withdrwal==1:
						withdrwal=float(input('Please enter the desired amount:'))
					elif option3==3:
						pay_in = float(input("How much would you like to pay"))
						balance = balance+pay_in
						print('\nYour balance is now $', balance)
						restart = input("would you like to go back")
						if restart in ('n', 'No', 'no', 'N'):
							print('Thank you for banking with Nepal Bank')
							break
						elif option4 ==4:
							print('Please wait while your card is returned....\n')
							print('Thank You')
							break
						else:
							print('Please enter a correct number. \n')
							restart = ('Yes')
				elif pin !=('1415'):
					print('Incorrect password')
					chances = chances=1
					if chances==0:
						print('\n No more tries, contact support jraikhola@gmail.com')
						break

			
							

