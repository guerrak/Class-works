import string

fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
alphabet = dict()
for line in fhandle:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            count += 1
            if letter not in alphabet:
                alphabet[letter] = 1
            else:
                alphabet[letter] += 1
t = list()
for key, val in list(alphabet.items()):
    t.append((val, key))
t.sort(reverse=True)
for key, val in t:
    print(key, val)
