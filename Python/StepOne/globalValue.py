x = 10
print(x)

def foo():
    global x # для того щоб вона стала глобальна
    print(x)
    x = 5
    print(x)


foo()
print(x)