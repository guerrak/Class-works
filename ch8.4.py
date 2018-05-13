fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'romeo.txt'
fhandle = open(fname)
t = list()
for line in fhandle:
    for i in line.split():
        if not i in t:
            t.append(i)
t.sort()
print(t)
