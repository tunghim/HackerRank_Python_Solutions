import re
S = input()
k = input()
pattern = re.compile(k)
m = re.search(pattern, S)
if not m:
    print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(), m.end() - 1))
    m = pattern.search(S, m.start() + 1)