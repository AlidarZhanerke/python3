import re

text = input()
pattern = r'ab*$'
match = re.search(pattern, text)
print(match.group())
# * - zero or more occurrences