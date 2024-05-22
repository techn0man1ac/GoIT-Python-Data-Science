class LessThanZero(Exception):
    pass
    # def __init__(self, value):
    #     self.value = value
    #
    # def __str__(self):
    #     return repr(self.value)

def func(n):
    if n < 0:
        raise LessThanZero(f'value {n} < 0')
    print(n)

func(-1)