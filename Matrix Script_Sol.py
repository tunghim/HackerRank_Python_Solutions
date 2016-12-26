import re

# Import original script
matrix = list()
n, m = map(int, input().split())
for _ in range(n):
    matrix.append(list(input()))

# Prep regex sample
sample = str()
for subset in list(zip(*matrix)):
    for letter in subset:
        sample += letter

# Substitute invalid characters with a space
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))
