s = input()
numbers = s.split('+')

numbers = [int(n) for n in numbers]
numbers.sort()
output = ""
for n in numbers:
    output += str(n) + "+"

print(output[:-1])
