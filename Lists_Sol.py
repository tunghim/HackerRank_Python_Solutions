# Using Python 2
arr = []
n = int(input())
for _ in range(n):
    str = raw_input().split(" ")
    cmd = str[0]
    if cmd == "insert":
        i = int(str[1])
        e = int(str[2])
        arr.insert(i, e)
    elif cmd == "print":
        print(arr)
    elif cmd == "remove":
        e = int(str[1])
        arr.remove(e)
    elif cmd == "append":
        e = int(str[1])
        arr.append(e)
    elif cmd == "sort":
        arr.sort()
    elif cmd == "pop":
        arr.pop()
    elif cmd == "reverse":
        arr.reverse()