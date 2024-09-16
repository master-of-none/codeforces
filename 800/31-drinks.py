n = int(input())
array = list(map(int, input().split()))

res = 0
for a in array:
    res += a

print(res/n)