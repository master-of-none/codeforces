n = int(input())
statement = [input() for _ in range(n)]

count = 0

for s in statement:
    if s == "++X":
        count += 1
    elif s == "X++":
        count += 1
    elif s == "--X":
        count -=1
    elif s == "X--":
        count -= 1

print(count)