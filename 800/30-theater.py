n,m,a = map(int, input().split())

flag_n = (n + a - 1) // a
flag_m = (m + a - 1) // a

res = flag_n * flag_m
print(res)