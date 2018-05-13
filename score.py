def computegrade(score):
    if score>1.0 or score<0.0:
        p = ('Bad score')
    elif score >= 0.9:
        p = ('A')
    elif score >= 0.8:
        p = ('B')
    elif score >= 0.7:
        p = ('C')
    elif score >= 0.6:
        p = ('D')
    elif score < 0.6:
        p = ('F')
    return p 
try:
	score = float(input('Enter a score between 0.0 and 1.0: \n'))
	p = computegrade(score) 
	print(p)
except:
	print("Bad score")
