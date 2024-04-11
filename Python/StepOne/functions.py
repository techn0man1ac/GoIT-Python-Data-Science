# Вигляд по всім вимогам з використанням вхідних параметрів

def add(value_one: int, value_two: int) -> int:
    """
    Function af adding two numbers

    Input:
    :param value_one: integer
    :param value_two: integer

    Output:
    :return: integer
    """
    sum_of_two_numbers = value_one + value_two
    return sum_of_two_numbers

result: int = add(123456, 3332)
print(result)

def print_input(value, *transport, **text):
    print(value)
    print(transport)
    print(text)
    print(text['may']/9)
    #print(hello)

print_input(78, 246, 'qwerty', 'iuagfioaggli;as', 346346346, 50, hello="Python", may=45)

def print_input(*transport, value, **text):
    print(value)
    print(transport)
    print(text)
    print(text['may']/9)

print_input(78, 246, 'qwerty', 'iuagfioaggli;as', 346346346, 50, hello="Python", may=45)