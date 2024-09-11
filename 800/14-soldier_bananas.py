k, n, w = map(int, input().split())

res = 0
i = 1
while w > 0:
    res = res + (k * i)
    i += 1
    w -= 1

print(res-n if res - n > 0 else 0)