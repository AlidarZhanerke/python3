import re

text = input()
pattern = r'[A-Z][a-z]+'
match = re.findall(pattern, text)
print(match.group())