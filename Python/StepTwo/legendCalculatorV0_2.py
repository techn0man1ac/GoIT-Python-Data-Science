'''
Legend Python calculator by Serhii Trush
V 0.2 
'''

def mathMagic(val0:float, oper:str, val1:float) -> str: # need to return String
    if (oper == "/" or oper == "//") and val1 == 0: #print(f'op. == "/" {oper == "/"} op. == "//" {oper == "//"} val.1 == 0 {val1 == 0} ')
        output = 'Error, divide by zero'
    else:
        match oper:
            case '+':
                output = val0 + val1
            case '-':
                output = val0 - val1
            case '*':
                output = val0 * val1
            case '**':
                output = val0 ** val1
            case '/':
                output = val0 / val1    
            case '//':
                output = val0 // val1
            case '%':
                output = val0 % val1
            case _:
                output = 'Error, unknown operation' 
    return output

try: # make exeption - protect wrong user input
    print(mathMagic(float(input("Value 1 = ")), input("Operation(+, -, *, **, /, //, %): "), float(input("Value 2 = "))))

except ValueError:
    print("Value 1/Value 2 is not a number")

finally:
    print("Thank's, goodbye")