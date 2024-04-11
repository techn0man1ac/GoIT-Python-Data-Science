password = 1234

def security(passwd):
    def divide():
        nonlocal passwd
        print(password)
        return passwd /2
    return divide()

print(security(password))