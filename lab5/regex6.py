import re
text = input()
x = text
x = re.sub('\s', ':', text)
x = re.sub('[.]', ':', x)
x = re.sub(',', ':', x)
print(x)