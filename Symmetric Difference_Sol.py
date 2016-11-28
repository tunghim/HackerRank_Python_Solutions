M = input()
# Me - M's elements
Me = set(map(int, input().split(' ')))
N = input()
# Ne - N's elements
Ne = set(map(int, input().split(' ')))
# res - result
res = sorted(Me.difference(Ne).union(Ne.difference(Me)))
print(*res, sep='\n')