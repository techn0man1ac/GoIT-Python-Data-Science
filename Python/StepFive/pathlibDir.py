from pathlib import Path
import time
directory = Path('Python/StepFive/new_folder') # Створює каталог
directory.mkdir(parents=True, exist_ok=True)
time.sleep(5) # Чекаєм 5 сек
directory = Path('Python/StepFive/new_folder') # Видаляє каталог
directory.rmdir()