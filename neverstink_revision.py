filter2 = open(r'C:\Users\danie\OneDrive\vscode\learning-python\UpdatedNeverStink1.3.txt' , 'w')
output = []
rules = ("Show" , "Hide")


with open(r'C:\Users\danie\OneDrive\vscode\learning-python\NeverStink1.3.txt', 'r') as filter1:
    for line in filter1:
        if line.startswith(rules):
            output.append("\n")
        if not line.startswith('#') and line.strip():
            output.append(line)

filter2.writelines(output)
