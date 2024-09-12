n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

count = 0
for i in range(n):
    sub = 0
    for j in range(len(array[i])):
        sub = array[i][j] - sub
    
    if sub >= 2:
        count += 1

print(count)