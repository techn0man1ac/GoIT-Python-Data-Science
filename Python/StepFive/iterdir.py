from pathlib import Path

# Створення об'єкту Path для директорії
directory = Path("./Python")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)

'''
Python\StepFive
Python\StepFour
Python\StepOne
Python\StepSix
Python\StepThree
Python\StepTwo
Python\test.py
Python\ZeroSteps
'''

