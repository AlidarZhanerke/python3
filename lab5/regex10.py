import re

text = input()
pattern = re.sub(r'([A-Z][a-z]+)', r' \1', text).strip()

pattern = pattern.split(' ')
str = ''
for i in range(0, len(pattern)):
    str += pattern[i].lower() + '_'
print(str[:-1])

