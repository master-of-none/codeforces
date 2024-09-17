n = int(input())
s = input()

s = s.lower()
freq = [0] * 26

for c in s:
    freq[ord(c) - ord('a')] += 1

count_0 = 0
for n in freq:
    if n == 0:
        count_0 += 1

print("NO") if count_0 >=1 else print("YES")