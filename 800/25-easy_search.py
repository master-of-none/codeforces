n = int(input())
array = list(map(int, input().split()))

hashset = set(array)
if 1 in hashset:
    print("HARD")

else:
    print("EASY")