import re

text = input()

pattern = re.sub(r'([A-Z][a-z]+)', r' \1', text).strip()
print(pattern)