A = set(input().split())
count = []
for i in range(int(input())):
    B = set(input().split())
    count.append(A.issuperset(B))
print(all(count))