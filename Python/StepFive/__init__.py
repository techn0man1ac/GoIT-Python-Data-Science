class Foo:
    def __init__(self, value=None):
        self.value = self.add_value(value)
        self.print_text()

    def print_text(self):
        print('print_text')

    def add_value(self, value):
        return value + 60

test = Foo(15)
print(test.value)