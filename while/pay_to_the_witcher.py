money = int(input())
counter = 0
while money >= 25:
    counter += 1
    money -= 25
while 10 <= money <= 25:
    counter += 1
    money -= 10
while 5 <= money <= 10:
    counter += 1
    money -= 5
while 1 <= money <= 5:
    counter += 1
    money -= 1
print(counter)