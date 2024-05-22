from collections import UserDict

class PositiveNumber(UserDict):

    def __getitem__(self, idx=None):
        if idx is None:
            return self.data
        return self.data[idx]

    def __setitem__(self, key, value):
        if value > 0:
            self.data[key] = value


numbers=PositiveNumber()

numbers[3] = 1
numbers[1] = -3
numbers[None] = 5
numbers[2] = 7

print(numbers[2])
print(numbers)
