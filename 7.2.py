fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
count = 0
total = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        atpos = line.find(':')
        num = float(line[atpos+ 1:-1])
        total = total+num
average=total/count
print('Average spam confidnece: ', average)
