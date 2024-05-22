from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("Python/StepFive/examplePl.txt")
absolute_path = relative_path.absolute()

current_working_directory = Path("C:/Projects/vscode-basics/GoIT-Python-Data-Science")
relative_path = absolute_path.relative_to(current_working_directory) # Python\StepFive\examplePl.txt
print(relative_path)

'''
Існує метод relative_to() який навпаки, використовується для 
отримання відносного шляху відносно заданої директорії.
'''
