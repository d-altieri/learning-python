import re

text = '''
'''

lines = text.splitlines()
pattern = r"\w{8}_\d{2}LAB"
match = re.search(pattern, text)

if match:
    print(match.group())
else:
    print("No equipment found")