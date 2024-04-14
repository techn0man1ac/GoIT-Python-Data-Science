value0 = float(input("Value 1 = "))
operation = input("Operation(+, -, *, **, /, //, %): ")
value1 = float(input("Value 2 = "))

output = ''

if operation == '+':
   output = value0 + value1
elif operation == '-':
   output = value0 - value1
elif operation == '*':
   output = value0 * value1
elif operation == '**':
   output = value0 ** value1
elif operation == '/':
   output = value0 / value1
elif operation == '//':
   output = value0 // value1
elif operation == '%':
   output = value0 % value1

print(output)