a = input()
b = input()
s = input()

hashmap = {}
for c in a:
    hashmap[c] = 1 + hashmap.get(c, 0)

for c in b:
    hashmap[c] = 1 + hashmap.get(c, 0)

for c in s:
    if c in hashmap:
        hashmap[c] -= 1
    else:
        hashmap[c] = -1

flag = False
for n, c in hashmap.items():
    if c != 0:
        flag = True
        break

if flag:
    print("NO")
else:
    print("YES")