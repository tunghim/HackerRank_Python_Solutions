import re
for _ in range(int(input())):
    res = True
    try:
        re.compile(input())
    except re.error:
        res = False
    print(res)