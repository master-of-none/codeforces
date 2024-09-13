n = int(input())

magnets = []
res = 1
for _ in range(n):
    magnets.append(int(input()))

for i in range(1, n):
    if magnets[i] != magnets[i-1]:
        res += 1

print(res)