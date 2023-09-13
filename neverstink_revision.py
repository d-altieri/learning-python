filter2 = open(r'C:\Users\danie\OneDrive\vscode\learning-python\UpdatedNeverStink1.3.txt' , 'w')

with open(r'C:\Users\danie\OneDrive\vscode\learning-python\NeverStink1.3.txt', 'r') as filter1:
    for line in filter1:
        if line.startswith('#'):
            continue
        else:
            filter2.writelines([line])
