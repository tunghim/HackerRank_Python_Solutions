from itertools import combinations

N = int(input())
L = input().split()
K = int(input())
count = 0

C = list(combinations(L, K))
fC = float(len(C))
for i in C:
    if 'a' in i:
        count += 1
print(float(count) / fC)