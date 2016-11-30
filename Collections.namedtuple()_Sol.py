from collections import namedtuple
N, Student = int(input()), namedtuple('Student', input())
Avg = sum(float(Student(*input().split()).MARKS) for _ in range(N)) / N
print("%.2f" % Avg)