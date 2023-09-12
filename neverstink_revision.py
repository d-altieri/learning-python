filter2 = open(r'C:\Users\daltier1\OneDrive - T-Mobile USA\Visual Studio\python\UpdatedNeverStink1.2.txt' , 'w')

with open(r'C:\Users\daltier1\OneDrive - T-Mobile USA\Visual Studio\python\NeverStink1.2.txt', 'r') as filter1:
    for line in filter1:
        if line.startswith('#'):
            continue
        line = line.rstrip()
        filter2.write(line)

filter2.close()
