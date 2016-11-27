# Python 2
s = raw_input()
i, c = raw_input().split()
i = int(i)
print s[:i] + c + s[i+1:]