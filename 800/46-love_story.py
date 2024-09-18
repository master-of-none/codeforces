n = int(input())

s = "codeforces"
s_list = list(s)

for _ in range(n):
    res = 0
    comp_string = list(input())

    for c in range(len(comp_string)):
        if comp_string[c] != s_list[c]:
            res += 1

    print(res)
