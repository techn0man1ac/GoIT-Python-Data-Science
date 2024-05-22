def decorator(func):
    def inner(arg_one, arg_two):
        print('Hellooooo')
        func(arg_one, arg_two)
        print('Goodbyyyeeee')
    return inner

@decorator
def full_name(name, surname):
    print(f'My name is {name} {surname}')

full_name('Serhii', 'Trush')

full_name('Serhii', 'Trush')
# decorator(full_name('Serhii', 'Trush'))