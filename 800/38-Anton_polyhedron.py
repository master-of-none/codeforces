n = int(input())

hashmap = {"Tetrahedron":4, "Cube":6, "Octahedron": 8, "Dodecahedron":12, "Icosahedron":20}

figures = []
for i in range(n):
    figures.append(input())

res = 0
for w in figures:
    res += hashmap[w]

print(res)