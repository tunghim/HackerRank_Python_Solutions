fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
fibs = lambda n: map(fib, range(n))
cubes = lambda x: map(lambda a: a**3, x)
print(list(cubes(fibs(int(input())))))