count = 0
found = False
while True:
    name = input()
    if name == 'Александра':
        found = True
    elif name == 'Левон':
        print(count)
        break
    elif found:
        count += 1