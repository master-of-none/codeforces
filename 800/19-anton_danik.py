n = int(input())
s = input()

anton_win = 0
danik_win = 0

for c in s:
    if c == 'A':
        anton_win += 1
    elif c == 'D':
        danik_win += 1

if anton_win > danik_win:
    print("Anton")
elif danik_win > anton_win:
    print("Danik")
else:
    print("Friendship")