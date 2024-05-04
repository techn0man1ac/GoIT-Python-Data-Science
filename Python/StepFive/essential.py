message = 'Goodbye'
def outer_func(name):
    message = 'Hello'
    def inner_func(message, name):
        return f'{message} {name}'
    return inner_func(message, name)

print(message)
print(outer_func('Serhii'))