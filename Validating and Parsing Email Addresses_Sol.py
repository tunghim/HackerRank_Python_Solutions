import re
for _ in range(int(input())):
    e = input()
    if re.search(r'<[a-z][\w.-]+@[a-z]+\.[a-z]{1,3}>', e, re.I):
        print(e)