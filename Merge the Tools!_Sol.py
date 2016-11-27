# Python 3
s = input()
k = int(input()) 
for i in zip(*[iter(s)] * k):
    dictionary = dict()
    print(''.join([dictionary.setdefault(c, c) for c in i if c not in dictionary]))