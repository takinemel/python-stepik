m = int(input())
p = int(input())
n = int(input())

population = m
for day in range(1, n + 1):
    print(day, population)
    population *= (1 + p / 100)