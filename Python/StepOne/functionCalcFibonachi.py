def fibonachi(number):
    return number if number == 0 or number == 1 else fibonachi(number-2) + fibonachi(number-1)

print(fibonachi(50))