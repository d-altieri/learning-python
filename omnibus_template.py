### Omnibus maintenance template ###

number_of_sites = int(input('How many hub sites? '))

output = []
nest_output = []

while number_of_sites > 0:
    hubs = input('Enter Hub ID: ').upper()
    sectors = input('Enter affected sectors: ').split(' ')
    output.append(f'{hubs}')
    nest_output.append(f'{hubs}')
    for sector in sectors:
        output.append(f'{hubs}_{sector}1LAB - 2100 | 1900 | LAA')
        continue
    output.append('')
    number_of_sites -= 1


print('''


==============================================
=================    NEST    =================
==============================================
''')
print(*nest_output, sep='\n')

print('''


===============================================
================   HANDOVER   =================
===============================================


PoC:


Alarms:


Following sectors and frequencies have been locked:
''')

print(*output, sep='\n')
