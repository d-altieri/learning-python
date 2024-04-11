filter2 = open(r'./UpdatedNeverStink1.5.filter', 'w')
output = []
rules = ("Show" , "Hide")


with open(r'./NeverStink1.5.filter', 'r') as filter1:
    for line in filter1:
        if line.startswith(rules):
            output.append("\n")
        if not line.startswith('#') and line.strip():
            output.append(line)

filter2.writelines(output)
