s1 = input()
s2 = input()
if len(s1) != len(s2):
    print("NO")
else:
    flag = True

    l = 0
    r = len(s2)-1
    while l < len(s1):
        if s2[r] != s1[l]:
            flag = False
            break
        l += 1 
        r -= 1

    if flag:
        print("YES")
    else:
        print("NO")