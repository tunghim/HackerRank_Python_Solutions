N, X = map(int, input().split())
marks = []
for i in range(X):
    marks.append(map(float, input().split()))
print(*[sum(student)/len(student) for student in zip(*marks)], sep="\n")