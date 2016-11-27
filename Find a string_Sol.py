# Using Python 2
str = raw_input()
subStr = raw_input()
count = 0
for i in range(len(str)):
   if str[i:i+len(subStr)] == subStr:
        count += 1
print count