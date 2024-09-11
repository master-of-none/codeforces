s = input()

upper_count = 0
lower_count = 0

for c in s:
    if ord(c) in range(ord('a'), ord('z')+1):
        lower_count += 1
    elif ord(c) in range(ord('A'), ord('Z')+1):
        upper_count += 1

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
    