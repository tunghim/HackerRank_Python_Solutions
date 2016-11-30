from itertools import product

K, M = map(int, input().split())
array = [map(int, input().split()[1:]) for _ in range(K)]

def f(nums):
    return sum(x * x for x in nums) % M

print(max(list(map(f, list(product(*array))))))