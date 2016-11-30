from collections import Counter

X = int(input())
sizeList = Counter(map(int, input().split()))
N = int(input())
money = 0
for _ in range(N):
    size, price = map(int, input().split())
    if sizeList[size]:
        money += price
        sizeList[size] -= 1
print(money)