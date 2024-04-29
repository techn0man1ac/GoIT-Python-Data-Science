from collections import defaultdict

phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636', '0509993637', '0639993636', '0509993632', '0339993632']

phone_operators_number = defaultdict(list)

for phone in phone_numbers:
    if phone.startswith('050') or phone.startswith('095'):
        phone_operators_number['Vodafone'].append(phone)
    elif phone.startswith('067') or phone.startswith('096'):
        phone_operators_number['Kyivstar'].append(phone)
    elif phone.startswith('063') or phone.startswith('093'):
        phone_operators_number['Lifecell'].append(phone)
    else:
        phone_operators_number['Other_operators'].append(phone)

print(phone_operators_number)
print(phone_operators_number.get('Kyivstar'))
print(phone_operators_number.get('Kyivstars'))
print(phone_operators_number)