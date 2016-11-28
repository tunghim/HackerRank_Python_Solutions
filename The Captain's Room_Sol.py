K = int(input())
rmNum = list(map(int, input().split()))
distinctRmNum = set(rmNum)
print(int((sum(distinctRmNum) * K - sum(rmNum)) / (K - 1)))