n = int(input())
list = raw_input().split()

for i in xrange(n):
        list[i] = int(list[i])
        
a = max(list)

while max(list) == a:
    list.remove(max(list))

print max(list)