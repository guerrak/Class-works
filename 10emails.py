fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    if not len(words) == 0 and words[0] == 'From':
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1

# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)

for key, val in lst[:10]:   # I could changed to 1st 3 / replace 3 with 1 to get only top 1
    print(key, val)
