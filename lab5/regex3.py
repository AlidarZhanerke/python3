import re

text = input()
pattern = r'[a-z]+_*[a-z]+'
match = re.findall(pattern, text)
print(match)