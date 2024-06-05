import shutil
from pathlib import Path

# Вихідний і цільовий файли
source = Path('Python/StepFive/exampleCpFls.txt')
destination = Path('Python/StepFive/pathlib/file1.txt')

# Копіювання файла
shutil.copy(source, destination)

'''
Функція shutil.copy() копіює вміст файлу, але не копіює метадані, 
тоді як shutil.copy2() копіює і вміст, і метадані.
Для переміщення файлів використовується функція shutil.move().
'''

# Вихідний і цільовий шляхи
source = Path('Python/StepFive/exampleCpFls.txt')
destination = Path('Python/StepFive/pathlib/file1.txt')

# Переміщення файла
shutil.move(source, destination)