from collections import UserList
from random import randint

class ExperimentsResults(UserList):

    def positive_values(self):
        return list(filter(lambda x: x >= 0, self.data))

    def negative_values(self):
        return list(filter(lambda x: x < 0, self.data))


result = ExperimentsResults()

for _ in range(20):
    result.append(randint(-10, 10))

print(result)
print(result.positive_values())
print(result.negative_values())
print(result.data)
'''
[-4, 1, 6, -7, 10, 0, -7, -8, 6, 5, 5, -7, -6, -5, -7, 7, -10, 2, 2, 1]
[1, 6, 10, 0, 6, 5, 5, 7, 2, 2, 1]
[-4, -7, -7, -8, -7, -6, -5, -7, -10]
[-4, 1, 6, -7, 10, 0, -7, -8, 6, 5, 5, -7, -6, -5, -7, 7, -10, 2, 2, 1]
'''

class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image= image

    def __repr__(self):
        return f"{self.real} - {self.image}i"

    def __str__(self):
        return f"{self.real} + {self.image}i"



number = Complex(10, 20)
print(number)
print(str(number))
print(repr(number))