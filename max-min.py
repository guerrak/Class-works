largest = 0
smallest = 0
while True:
    try:
        inp = input('Enter a number: ')
        if inp == 'done':
            break
        n = int(inp)
        if largest < n:
            largest = n
        if smallest == 0 or smallest > n:
            smallest = n
    except:
        print('Invalid input')
    # print inp
print('Maximum is', largest)
print('Minimum is', smallest)
