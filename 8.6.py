numbers = []
while True:
    inp = input('Enter a number: ')

    if inp == 'done':
        break
    else:
        try:
            inp = int(inp)
            inp = float(inp)
            numbers.append(inp)
        except:
            print('Invalid input')
            exit()

print('Maximum:', max(numbers))
print('Minimum:', min(numbers))
