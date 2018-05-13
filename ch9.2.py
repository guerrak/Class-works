fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
days = dict()
for line in fhandle:
    if line.startswith('From '):
        line = line.split()
        day = line[2]
        days[day] = days.get(day, 0) + 1
print(days)
