import re
input = input()
print(bool(re.match(r'^[1-9]\d{5}$', input) and not(re.search(r'(?<=(\d))\d(?=\1).*(?<=(\d))\d(?=\2)', input))))
