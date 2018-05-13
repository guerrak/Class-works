def computepay(h,r):
	if (h > 40):
		value = (((h - 40) * 1.5)+ 40) * r 
	else:
		value = h * r
	return value 
prompt = 'What is your gross pay? Enter Hours: \n'
hours = int(input(prompt))
rate = float(input("Enter Rate: "))
try:
	hours = float(hours)
	rate = float(rate)
except:
	print('Enter a valid float value')
	quit()
p = computepay(hours,rate)
print(p) 