n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold_score = scores[k-1]
count = 0

for n in scores:
    if n >= threshold_score and n > 0:
        count += 1

print(count)

