n = int(input())
count = 0

for _ in range(n):
    problems = list(map(int, input().split()))

    if sum(problems) >= 2:
        count += 1

print(count)

