def greeting(variable):
    print(f'Function greeting with variable {variable}')
greeting('Bob')

def bot(func):
    def inner_func(*args, **kwargs):
        print('Hello')
        result = func(*args, **kwargs)
        print('Goodbye')
        return result
    return inner_func

bot_says = bot(greeting)
bot_says('TEST')
