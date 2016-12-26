import re
for _ in range(int(input())):
    m = re.findall(r'#[a-fA-F\d]{6}|#[a-fA-F\d]{3}', input()[1:])
    if m:
        print(*m, sep='\n')