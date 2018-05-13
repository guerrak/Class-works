fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
words = dict()
ftext = fhandle.read()
wordlist = ftext.split()
for word in wordlist:
    words[word] = 0
while True:
    check = input('Enter word: ')
    if check == 'I am done':
        break
    else:
        print(check in words)
