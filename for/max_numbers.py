n = int(input())
max1 = int(input())
max2 = int(input())
if max1 < max2:
    max1, max2 = max2, max1
for _ in range(n - 2):
    x = int(input())
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
print(max1)
print(max2)