# Python 3
import string
alphabet = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alphabet[i:n])
    L.append((s[::-1] + s[1:]).center(4 * n-3, "-"))

print('\n'.join(L[:0:-1] + L))