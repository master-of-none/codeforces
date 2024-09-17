n = list(map(int, input().split()))

n_set = set(n)
res = 4 - len(n_set)
print(res)