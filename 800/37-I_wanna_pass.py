n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

p_set = set(p[1:])
q_set = set(q[1:])

all_levels = p_set.copy()
all_levels.update(q_set)

flag = True
for i in range(1, n+1):
    if i not in all_levels:
        flag = False
        break

if flag:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
