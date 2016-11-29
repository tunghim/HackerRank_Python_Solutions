a, b = (int(input()) for _ in range(2))
print("{0}\n{1}\n({0}, {1})".format(*divmod(a, b)))