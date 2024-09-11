n = input()

count = 0
for c in n:
    if c == '4' or c == '7':
        count += 1

res = 0
for c in str(count):
    if c not in '7' and c not in '4':
        res += 1

print("YES" if res <= 0 else "NO")