import re
addr = re.compile(
    '''^
    [\w-]{1,}           #username
    @[a-zA-Z0-9]{1,}    #websitename
    \.\w{1,3}           #extension
    $''', re.UNICODE | re.VERBOSE)
print(sorted(filter(addr.search, (input() for _ in range(int(input()))))))