import re

text = '''skdjghaskjghla03453ba1230-93905u2345
'''

lines = text.splitlines()
pattern = r"\w{8}_\d{2}LAB"
match = re.findall(pattern, text)
result = sorted(match)

if match:
    print(*result, sep="\n")
else:
    print("No equipment found")