from itertools import groupby

for c, x in groupby(input()):
    print((len(list(x)), int(c)), end=' ')