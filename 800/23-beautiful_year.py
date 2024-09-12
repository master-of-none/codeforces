s = input()

res = int(s) + 1
while True:
    if len(set(str(res))) == len(str(res)):
        break
    
    res += 1
print(res)