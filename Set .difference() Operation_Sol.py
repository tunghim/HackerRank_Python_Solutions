n = int(input())
Eng = set(input().split())
b = int(input())
Fr = set(input().split())
print(len(set(Eng.difference(Fr))))