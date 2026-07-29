n = int(input())
total = 0
found = False
for i in range(1, n + 1):
    square = i**2
    last_digit = square % 10
    if last_digit == 2 or last_digit == 5 or last_digit == 8:
        total = total + i
        found = True
if found:
    print(total)
else:
    print(0)
