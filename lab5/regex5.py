import re

text = input()
pattern = r'a.*b$'
match = re.findall(pattern, text)
print(match)