x = 50

def func() -> None:
    x = 2
    print('Local X to', x)  # x -> 2

func()
print('Global X the same ', x)  # x = 50

def outer_func():
    enclosing_var = "I variable"

    def inner_func():
        print("Inside inner_func():", enclosing_var)

    inner_func()

outer_func()

def func_outer(): # Enclosing
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x

result = func_outer() 
print('LEGB result ', x) # LEGB result 5

x = 50

def func():
    global x
    print('X =', x)  # x = 50
    x = 2
    print('Change X to', x)  # Change x to 2

func()
print('X = ', x) # X = 2