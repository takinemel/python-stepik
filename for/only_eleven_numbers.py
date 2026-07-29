found = False
for i in range(10):
    number = int(input())
    if number % 2 != 0: 
        found = True
        break

if found:
    print('NO')
else:
    print('YES')