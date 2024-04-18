'''
Факторіал натурального числа n (позначається як n!) — 
це добуток всіх натуральних чисел від 1 до n включно
'''

def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(int(input("Set number: ")))) # Set number: 5 виведе 120