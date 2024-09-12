n,t = map(int, input().split())
s = input()

s_list = list(s)
for _ in range(t):
    i = 0
    while i < n - 1:
        if s_list[i] == "B" and s_list[i+1] == "G":
            s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
            i += 1
        i += 1
    
print(''.join(s_list))