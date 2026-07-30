count = 0
number = int(input())
while 0 < number < 6:
    if number == 5:
        count += 1
    number = int(input())
print(count)