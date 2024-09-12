n = int(input())
stops = [tuple(map(int, input().split())) for _ in range(n)]

passengers = 0
maxP = 0
for i in range(n):
    a, b = stops[i]
    passengers -= a
    passengers += b
    maxP = max(passengers, maxP)

print(maxP)