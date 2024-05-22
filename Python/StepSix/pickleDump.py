from pickle import dumps, loads


class Absolute:
    value = 'some_data'

    def __init__(self):
        print('New A!')
        self.data = 'another'

instance = Absolute()

serialization_instance = dumps(instance)
serialization_Absolute = dumps(Absolute)

restored_instance = loads(serialization_instance)
restored_Absolute = loads(serialization_Absolute)

print(instance.value, instance.data)
print(restored_instance.value, restored_instance.data)
print(dir(restored_Absolute))
print(restored_Absolute.__dict__)

test_instance = restored_Absolute()
print(test_instance.__dict__)

'''
Запис цілого класу у бінарному форматі
'''