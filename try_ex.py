prompt = 'What is your gross pay? Enter Hours: \n'
try:
	hours = int(input(prompt))
	rate = float(input('Enter Rate: '))
	pay = hours*rate
	print("Pay: ", pay)
except:
	print('Error, please enter numeric input')
