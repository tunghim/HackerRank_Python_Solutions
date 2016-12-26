import re
for _ in range(int(input())):
    s = input()
    if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s):
        print('Valid')
    else:
        print('Invalid')