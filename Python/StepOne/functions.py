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