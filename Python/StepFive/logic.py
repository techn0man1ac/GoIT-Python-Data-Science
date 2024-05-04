def sum(a, b):
    return a+b

new_sum = sum

print(new_sum(2, 3))

def sum(a, b):
    return a+b

def operation(a, b, func):
    return func(a, b)

print(operation(5, 3, sum))

def sum(a, b):
    return a+b

def minus(a, b):
    return a-b

def power(a):
    return pow(a, 2)

def operation(operator):
    if operator == '+':
        return sum
    if operator == '-':
        return minus
    if operator == '*':
        return power


print(minus(7, 9))

sum_func = operation('+')
print(sum_func(9, 3))

sum_func = operation('-')
print(sum_func(9, 3))

sum_func = operation('*')
print(sum_func(9))