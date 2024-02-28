import re

text = input()
a = re.split('_', text)
for i in a:
    print(i, end = '')
