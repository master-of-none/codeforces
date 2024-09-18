array = list(map(int, input().split()))
array.sort()

mid = len(array) // 2

res = 0
for n in array:
    res += abs(n - array[mid])

print(res)
    