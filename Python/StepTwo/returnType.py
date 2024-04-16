def greet(name: str) -> str:
    return f"Hello, {name}!"

greeting = greet("Serhii")
print(greeting)  # Hello, Serhii!

def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(int(input("Number % 2 - ")))
print(check_even) 

def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum

result = add_numbers(float(input("Value 1 = ")), float(input("Value 2 = ")))
print(f"Summa = {result}")  # Виведе: 15