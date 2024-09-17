n = int(input())

array = []

for i in range(1, n+1):
    if i % 2 == 1:
        array.append("I hate")
    else:
        array.append("I love")

res = " that ".join(array) + " it"
print(res)