person = {'name': 'Serhii', "age": 32, "phone": "38(068)*********", 'student': False, 1243: ['test', 'failed']}
print(person)

new_data = {'location': 'Ukraine, Lutsk', 'lang': "ukr"}
person.update(new_data)
print(person)
print(person.get('name', 'Noname'))
print(person.get('lang', None))

person.pop(1243)
print(person)

person["age"] = 100
print(person)

person['test'] = True
print(person)

person.update({(1, ): False})
print(person)