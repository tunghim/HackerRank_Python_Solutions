import re
pattern = '^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
roman = str(input())
if re.search(pattern, roman):
    print('True')
else:
    print('False')