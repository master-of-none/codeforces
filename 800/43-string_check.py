n = int(input())

s = set("codeforces")

for i in range(n):
    c = input()
    if c in s:
        print("YES")
    else:
        print("NO")
