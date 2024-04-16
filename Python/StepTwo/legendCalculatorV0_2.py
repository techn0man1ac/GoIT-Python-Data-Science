'''
Legend Python calculator by Serhii Trush
V 0.2 
'''
value0 = 0.0
operation =''
value1 = 0.0

try:
    value0 = float(input("Value 1 = "))
    operation = input("Operation(+, -, *, **, /, //, %): ")
    value1 = float(input("Value 2 = "))

except ValueError:
    print("Value 1/Value 2 is not a number")
else:
    #print(f'op. == "/" {operation == "/"} op. == "//" {operation == "//"} val.1 == 0 {value1 == 0} ')

    if (operation == "/" or operation == "//") and value1 == 0:
        output = 'Error, divide by zero'
    else:
        match operation:
            case '+':
                output = value0 + value1
            case '-':
                output = value0 - value1
            case '*':
                output = value0 * value1
            case '**':
                output = value0 ** value1
            case '/':
                output = value0 / value1    
            case '//':
                output = value0 // value1
            case '%':
                output = value0 % value1
            case _:
                output = 'Error, unknown operation'

    print(output)

finally:
    print("End")