def outer_func(value):
    def inner_func(number):
        return value * number
    return inner_func


multiply_five = outer_func(5)
multiply_two = outer_func(2)

print(multiply_five(5), multiply_five(10))
print(multiply_two(7))