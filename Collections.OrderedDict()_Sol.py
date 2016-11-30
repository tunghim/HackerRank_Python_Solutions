from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    litem = input().split(' ')
    price = int(litem[-1])
    item_name = " ".join(litem[:-1])
    if d.get(item_name):
        d[item_name] += price
    else:
        d[item_name] = price

for i, v in d.items():
    print(i, v)