numA = int(input())
A = set(map(int, input().split()))
numN = int(input())
for _ in range(numN):
    op = input().split()
    N = set(map(int, input().split()))
    if op[0] == "update":
        A.update(N)
    elif op[0] == "intersection_update":
        A.intersection_update(N)
    elif op[0] == "difference_update":
        A.difference_update(N)
    elif op[0] == "symmetric_difference_update":
        A.symmetric_difference_update(N)
print(sum(A))