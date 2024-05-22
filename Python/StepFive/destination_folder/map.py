names = ['serhii', 'carl', 'paul', 'candymen']

normal_name = list(map(str.title, names))
print(normal_name)

def number_sqr(value):
    return pow(value, 2)

square_number = list(map(number_sqr, [i for i in range(10)]))
print(square_number)