matrix = []

for _ in range(5):
    matrix.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            x,y = i+1, j+1

res = abs(x-3) + abs(y-3)
print(res)
