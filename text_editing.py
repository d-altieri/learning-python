import re

text = ''''''

lines = text.splitlines()
re_pattern = r"(?P<mod_name>.*): (?P<mod_url>https.*)"
compiled_re_pattern = re.compile(re_pattern)

for line in lines:
    result = re.match(compiled_re_pattern, line)

    if result:
        mod_name = result["mod_name"]
        mod_url = result["mod_url"]

        print(f"{mod_name:<50}\t{mod_url}")