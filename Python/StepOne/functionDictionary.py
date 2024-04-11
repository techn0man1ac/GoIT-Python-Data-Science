def gretting(**kwargs): #  -> kwargs = {'key': value, ..... 'key_n': value_n}
    print(kwargs)
    name = kwargs.get("name", 'Unknown')
    age = kwargs.get("age", 33)
    print(f"Hello {name}, you are {age} years old")

gretting(name="Serhii")
gretting(name="Serhii", age=32)