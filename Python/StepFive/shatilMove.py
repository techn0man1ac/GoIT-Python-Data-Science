import shutil
from pathlib import Path

# Вихідний і цільовий шляхи
source = Path('Python/StepFive/exampleMove.txt')
destination = Path('Python/StepFive/pathlib/file2.txt')

# Переміщення файла
shutil.move(source, destination)