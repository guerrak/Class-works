count = 0
total = 0
while True:
    inp = input('Enter a number: ')
    # Handle the edge cases
    if inp == 'done':
        break
    if len(inp) < 1:
        break  # Check for empty line
    # Do the work
    try:
        number = float(inp)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + number
    print(number, total, count)
print('Average:', total / count)
