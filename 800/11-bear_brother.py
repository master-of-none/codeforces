b1, b2 = (map(int, input().split()))

n = 0

while True:
    b1 = b1 * 3
    b2 = b2 * 2
    n += 1
    if b1 > b2:
        break

print(n)