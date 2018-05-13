fname = input('Enter file name: ')
try:
    if fname == 'na na boo boo':
        print("Haha, you've been punk'd")
        exit()
    else:
        fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'Subject lines in', fname)
