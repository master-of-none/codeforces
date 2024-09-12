n, h = map(int, input().split())
array = list(map(int, input().split()))

res = 0
for val in array:
    if val <= h:
        res += 1
    else:
        res += 2
print(res)