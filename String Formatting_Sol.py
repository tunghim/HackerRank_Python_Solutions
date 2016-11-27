# Python 3
n = int(input())
width = len(bin(n)[2:])
for i in range(1, n + 1):
    print (str(i).rjust(width, ' '), str(oct(i)[2:]).rjust(width, ' '), str(hex(i)[2:].upper()).rjust(width,' '), bin(i)[2:].rjust(width,' '), sep=' ')