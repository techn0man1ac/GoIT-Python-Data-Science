from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("Python/StepFive/examplePl.txt")
absolute_path = relative_path.absolute() # C:\Projects\vscode-basics\GoIT-Python-Data-Science\Python\StepFive\examplePl.txt
print(absolute_path) 