fname = input("Enter file name: ")
if len(fname) == 0:
    fname = "mbox-short.txt"
fhandle = open(fname)
count = 0
for line in fhandle:
    line = line.rstrip()
    if line == " ":
        continue
    if line.startswith('From'):
        word = line.split()
        if(len(word)) > 2:
            print(word[1])
            count = count + 1

print('There were', count, 'lines in the file with From as the first word')
