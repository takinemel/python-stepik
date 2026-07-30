h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
current_h = h1
current_m = m1
while True:
    print(f"{current_h:02d}:{current_m:02d}")
    if current_h == h2 and current_m == m2:
        break
    current_m += 1
    if current_m == 60:
        current_m = 0
        current_h += 1