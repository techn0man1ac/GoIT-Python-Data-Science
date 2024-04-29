from decimal import Decimal

first_value = round(0.2 + 0.1 + 0.3 - 0.5, 17)
print(first_value)

second_value = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
print(second_value)

number_one = 1.37
number_two = 1.500000

first = Decimal.from_float(number_one)
print(first)

second = Decimal.from_float(number_two)
print(second)