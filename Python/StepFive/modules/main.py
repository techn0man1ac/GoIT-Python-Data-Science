# main.py
import mymodule

print(mymodule.say_hello("Serhii"))

# main.py
from mymodule import say_hello # Імпорт функції з mymodule.py

print(say_hello("World"))

# main.py
from mymodule import say_hello as greeting # Заміна функції say_hello на greeting
 
print(greeting("Greeting"))

#print(dir(greeting)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'greeting', 'mymodule', 'say_hello']
print(greeting("World"))