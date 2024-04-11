import re

text = '''T3LA1051 / LA0406BA_31LAB|TMB_CA_ExpoPark(LA02594A)_01(Small Cell)
'''


lines = text.splitlines()
re_pattern = r"/\w{8}_/\d{2}LAB"
compiled_re_pattern = re.compile(re_pattern)


print(compiled_re_pattern)